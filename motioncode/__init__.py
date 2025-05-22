# motion_code/__init__.py

__version__ = "0.1.0"

# Core motion‐forecast API
from .motion_code import MotionCode, motion_code_classify, motion_code_forecast
from .motion_code_utils import optimize_motion_codes, classify_predict_helper

# Data processing
from .data_processing import (
    clear,
    read_sound_timeseries,
    generate_data_from_sound_dataset,
    interp_parkison_data_for_benchmarking_algorithms,
    load_data,
    process_data,
    add_time_variable,
    process_data_for_motion_codes,
    split_train_test_forecasting,
    get_train_test_data_forecast,
    get_train_test_data_classify,
    randomly_remove_data_points,
    get_pronunciation_audio_data_unequal_lengths  # watch spelling here
)
from .parkinson_data_processing import (
    get_label_to_ids_map,
    get_refined_label_to_ids_map,
    get_parkinson_train_test_data_helper,
    get_parkinson_train_test_data
)

# Utilities & modeling helpers
from .utils import (
    accuracy,
    RMSE,
    forecast_means_vars,
    forecast_mean_vars_motion_codes,
    plot_timeseries,
    plot_motion_codes,
    plot_mean_covars,
    get_inducing_pts_for_individual_series
)
from .sparse_gp import (
    sigmoid,
    sigmoid_inv,
    softmax,
    softplus,
    softplus_inv,
    jitter,
    spectral_kernel,
    pack_params,
    unpack_params_single,
    unpack_params,
    elbo_fn_from_kernel,
    elbo_fn_single,
    elbo_fn,
    phi_opt,
    q
)

# Benchmarks
from .benchmarks import (
    run_classify_benchmark,
    run_forecast_benchmark,
    get_data_dict,
    main
)

__all__ = [
    "__version__",
    # motion_code
    "MotionCode", "motion_code_classify", "motion_code_forecast",
    "optimize_motion_codes", "classify_predict_helper",
    # data
    "clear", "read_sound_timeseries", "generate_data_from_sound_dataset",
    "interp_parkison_data_for_benchmarking_algorithms", "load_data",
    "process_data", "add_time_variable", "process_data_for_motion_codes",
    "split_train_test_forecasting", "get_train_test_data_forecast",
    "get_train_test_data_classify", "randomly_remove_data_points",
    "get_pronunciation_audio_data_for_unequal_lengths",
    # parkinson
    "get_label_to_ids_map", "get_refined_label_to_ids_map",
    "get_parkinson_train_test_data_helper", "get_parkinson_train_test_data",
    # utils
    "accuracy", "RMSE", "forecast_means_vars", "forecast_mean_vars_motion_codes",
    "plot_timeseries", "plot_motion_codes", "plot_mean_covars",
    "get_inducing_pts_for_individual_series",
    # sparse_gp
    "sigmoid", "sigmoid_inv", "softmax", "softplus", "softplus_inv",
    "jitter", "spectral_kernel", "pack_params", "unpack_params_single",
    "unpack_params", "elbo_fn_from_kernel", "elbo_fn_single", "elbo_fn",
    "phi_opt", "q",
    # benchmarks
    "run_classify_benchmark", "run_forecast_benchmark", "get_data_dict", "main",
]
