import argparse


def get_args(description="MILNCE"):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--log_root", type=str, default="/home/derekhmd/cs6998_05/data/logs", help="log dir root")
    parser.add_argument("--log_name", default="exp", help="name of the experiment for checkpoints and logs")
    parser.add_argument("--checkpoint_dir", type=str, default="/home/derekhmd/cs6998_05/data/checkpoints",
        help="checkpoint model folder",
    )
    parser.add_argument("--training_dataset", type=str, 
        # default="/home/derekhmd/cs6998_05/data/splits/2fps_augmented_80p_tvsum.txt",
        # default="/home/derekhmd/cs6998_05/data/splits/augmented_80ptvsum.txt"
        default="/home/derekhmd/cs6998_05/data/splits/n2_8fps.txt",
        # default="/home/derekhmd/cs6998_05/data/splits/debug.txt",
        # default="/home/derekhmd/cs6998_05/data/splits/2fps_20p_tvsum.txt",
        help="filepath for the training dataset",
    )
    parser.add_argument("--testing_dataset", type=str, 
        # default="/home/derekhmd/cs6998_05/data/splits/augmented_80ptvsum.txt",
        # default="/home/derekhmd/cs6998_05/data/splits/debug.txt",
        default="/home/derekhmd/cs6998_05/data/splits/20p_tvsum.txt",
        help="filepath for the testing dataset",
    )
    parser.add_argument("--optimizer", type=str, default="adam", help="opt algorithm")
    parser.add_argument("--weight_decay", "--wd",
        default=0.00001,
        type=float,
        metavar="W",
        help="weight decay (default: 1e-4)",
    )
    parser.add_argument("--num_thread_reader", type=int, default=4, help="")
    parser.add_argument("--checkpoint_cadence", type=int, default=10, help="Runs a model checkpoint every n epochs")
    parser.add_argument("--batch_size", type=int, default=16, help="batch size") # MAKE SURE THE DATASET IS DIVISIBLE BY THIS!
    parser.add_argument("--batch_size_val", type=int, default=10, help="batch size eval")
    parser.add_argument("--momemtum", type=float, default=0.9, help="SGD momemtum")
    parser.add_argument("--lr_step_size", type=int, default=100, help="Learning Rate Scheduler step size")
    parser.add_argument("--randomized_start", dest="randomized_start", type=bool, default=False, help="whether to always load videos at the starting segment")
    parser.add_argument("--debug_dataset_mode", dest="debug_dataset_mode", type=bool, default=False, help="dataset debugging")
    parser.add_argument("--freeze_base", dest="freeze_base", action="store_true", help="whether to freeze the TCLR backbone layer")
    parser.add_argument("--tclr_dim", type=int, default=512, help="The TCLR model dimensionality")
    parser.add_argument("--k", type=float, default=0.55, help="Top k percent of segments")
    parser.add_argument("--log_freq", type=int, default=1, help="Information display frequence")
    parser.add_argument(
        "--req_segment_count",
        type=int,
        default=56,
        help="required number of segments",
    )
    parser.add_argument(
        "--num_frames_per_segment",
        type=int,
        default=16,
        help="number of frames in each segment",
    )
    parser.add_argument("--enc_heads", "-enc_heads", default=4, type=int, help="number of transformer heads")
    parser.add_argument(
        "--enc_layers",
        "-enc_layers",
        default=4,
        type=int,
        help="number of layers in transformer encoder",
    )
    parser.add_argument(
        "--dropout", "--dropout", default=0.1, type=float, help="Dropout",
    )
    parser.add_argument("--verbose", dest="verbose", action="store_true")
    parser.add_argument(
        "--pretrain_tclr_path",
        type=str,
        default="/home/derekhmd/best_models/model_best_e269_loss_16.523.pth",
        help="",
    )
    parser.add_argument("--cudnn_benchmark", type=int, default=0, help="")
    parser.add_argument("--epochs", default=100, type=int, metavar="N", help="number of total epochs to run")
    parser.add_argument(
        "--start-epoch",
        default=0,
        type=int,
        metavar="N",
        help="manual epoch number (useful on restarts)",
    )
    parser.add_argument(
        "--lrb",
        "--learning-rate-base",
        default=0.00003,
        type=float,
        help="base learning rate",
        dest="lr_base",
    )
    parser.add_argument(
        "--lri",
        "--learning-rate-importance",
        default=0.00003,
        type=float,
        help="initial learning rate",
        dest="lr_importance",
    )
    parser.add_argument("--momentum", default=0.9, type=float, metavar="M", help="momentum")
    parser.add_argument(
        "--resume",
        dest="resume",
        action="store_true",
        help="resume training from last checkpoint",
    )
    parser.add_argument(
        "-e",
        "--evaluate",
        dest="evaluate",
        action="store_true",
        help="evaluate model on validation set",
    )
    parser.add_argument(
        "--pretrained",
        dest="pretrained",
        action="store_true",
        help="use pre-trained model",
    )
    parser.add_argument("--pin_memory", dest="pin_memory", action="store_true", help="use pin_memory")
    parser.add_argument(
        "--distributed",
        dest="distributed",
        action="store_true",
        help="distributed training",
    )
    parser.add_argument(
        "--world-size",
        default=1,
        type=int,
        help="number of nodes for distributed training",
    )
    parser.add_argument(
        "--local_rank", default=-1, type=int, help="local rank for distributed training"
    )
    parser.add_argument(
        "--dist-file",
        default="dist-file",
        type=str,
        help="url used to set up distributed training",
    )
    parser.add_argument(
        "--dist_url", default="env://", help="url used to set up distributed training"
    )
    parser.add_argument(
        "--dist-backend", default="nccl", type=str, help="distributed backend"
    )
    parser.add_argument(
        "--seed", default=1, type=int, help="seed for initializing training. "
    )
    parser.add_argument("--ngpus", default=0, type=int, help="Number of available gpus")
    parser.add_argument("--gpu", default=None, type=int, help="GPU id to use.")
    parser.add_argument("--rank", default=0, type=int, help="Rank.")
    parser.add_argument(
        "--multiprocessing-distributed",
        action="store_true",
        help="Use multi-processing distributed training to launch "
        "N processes per node, which has N GPUs. This is the "
        "fastest way to use PyTorch for either single node or "
        "multi node data parallel training",
    )
    args = parser.parse_args()
    return args
