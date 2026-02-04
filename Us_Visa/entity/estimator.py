from dataclasses import dataclass


@dataclass
class TargetValueMapping:
    """
    Target value mapping for classification.
    Update values according to your dataset.
    """
    approved: int = 1
    rejected: int = 0

    def to_dict(self) -> dict:
        return {
            "approved": self.approved,
            "rejected": self.rejected,
        }

    def reverse_mapping(self) -> dict:
        return {
            self.approved: "approved",
            self.rejected: "rejected",
        }
