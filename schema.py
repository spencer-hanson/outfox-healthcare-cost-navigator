from sqlalchemy import String, Integer, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Provider(Base):
    __tablename__ = "providers"
    provider_id: Mapped[int] = mapped_column(primary_key=True)
    provider_name: Mapped[str] = mapped_column(String(30))
    provider_city: Mapped[str] = mapped_column(String(30))
    provider_state: Mapped[str] = mapped_column(String(2))
    provider_zipcode: Mapped[str] = mapped_column(Integer())

    def __repr__(self):
        return f"Provider({self.provider_name})"


class Procedure(Base):
    __tablename__ = "procedure"
    procedure_id: Mapped[int] = mapped_column(primary_key=True)
    provider: Mapped[int] = mapped_column(ForeignKey("providers.provider_id"))
    average_covered_charges: Mapped[str] = mapped_column(Numeric(8))
    average_total_payments: Mapped[str] = mapped_column(Numeric(30))
    average_medicare_payments: Mapped[str] = mapped_column(Numeric(30))
    ms_drg_definition: Mapped[str] = mapped_column(String(255))
    total_discharges: Mapped[str] = mapped_column(Integer())

    def __repr__(self):
        return f"Procedure({self.procedure_id})"
