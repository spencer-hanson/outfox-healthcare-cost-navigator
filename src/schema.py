from sqlalchemy import String, Integer, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Provider(Base):
    __tablename__ = "providers"
    id: Mapped[int] = mapped_column(primary_key=True)
    provider_id: Mapped[int] = mapped_column(String(8))
    provider_name: Mapped[str] = mapped_column(String(255))
    provider_city: Mapped[str] = mapped_column(String(255))
    provider_state: Mapped[str] = mapped_column(String(2))
    provider_zipcode: Mapped[str] = mapped_column(Integer())

    def __repr__(self):
        return f"Provider({self.provider_name})"

    def to_json(self):
        return {
            "id": self.id,
            "provider_id": self.provider_id,
            "provider_name": self.provider_name,
            "provider_city": self.provider_city,
            "provider_state": self.provider_state,
            "provider_zipcode": self.provider_zipcode
        }


class Procedure(Base):
    __tablename__ = "procedure"
    procedure_id: Mapped[int] = mapped_column(primary_key=True)
    provider_fkey: Mapped[int] = mapped_column(ForeignKey("providers.id"))
    provider_id: Mapped[int] = mapped_column(String(8))
    average_covered_charges: Mapped[str] = mapped_column(Numeric(8))
    average_total_payments: Mapped[str] = mapped_column(Numeric(8))
    average_medicare_payments: Mapped[str] = mapped_column(Numeric(8))
    ms_drg_definition: Mapped[str] = mapped_column(String(255))
    total_discharges: Mapped[str] = mapped_column(Integer())

    def __repr__(self):
        return f"Procedure({self.procedure_id})"

    def to_json(self):
        return {
            "procedure_id": self.procedure_id,
            "provider_fkey": self.provider_fkey,
            "provider_id": self.provider_id,
            "average_covered_charges": self.average_covered_charges,
            "average_total_payments": self.average_total_payments,
            "average_medicare_payments": self.average_medicare_payments,
            "ms_drg_definition": self.ms_drg_definition,
            "total_discharges": self.total_discharges
        }
