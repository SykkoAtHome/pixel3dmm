"""Functions to execute the Pixel3DMM pipeline from Nuke."""

from pixel3dmm import env_paths
from scripts.run_preprocessing import main as run_preprocessing
from scripts.network_inference import main as run_inference
from scripts.track import main as run_tracking

from .utils import video_to_name


def _run_inference(video_name: str, prediction_type: str) -> None:
    try:
        from omegaconf import OmegaConf
    except ImportError as exc:
        raise ImportError(
            "OmegaConf is required for inference. Install it with 'pip install omegaconf'."
        ) from exc

    cfg = OmegaConf.load(f"{env_paths.CODE_BASE}/configs/base.yaml")
    cfg.model.prediction_type = prediction_type
    cfg.video_name = video_name
    run_inference(cfg)


def _run_tracking(video_name: str) -> None:
    try:
        from omegaconf import OmegaConf
    except ImportError as exc:
        raise ImportError(
            "OmegaConf is required for tracking. Install it with 'pip install omegaconf'."
        ) from exc

    cfg = OmegaConf.load(f"{env_paths.CODE_BASE}/configs/tracking.yaml")
    cfg.video_name = video_name
    run_tracking(cfg)


def run_full_pipeline(video_or_images_path: str) -> None:
    """Run preprocessing, inference and tracking."""
    run_preprocessing(video_or_images_path)
    name = video_to_name(video_or_images_path)

    for pred in ("normals", "uv_map"):
        _run_inference(name, pred)

    _run_tracking(name)
