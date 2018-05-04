from argparse import ArgumentParser
import logging
from pathlib import Path
from ShallowNetworks.src.ConvolutionalNeuralNetwork import POOLING_SIZE, KERNEL_SIZE, NUM_FILTERS, NUM_LAYERS, NUM_FOLDS, NUM_EPOCHS, IMG_DIMENSION


def setup():
    """
    Setup for running the project
    :return: Parsed Arguments
    """
    parser = ArgumentParser()
    parser.add_argument("image_directory", type=str, help="Location of images")
    parser.add_argument(
        "--pooling_size",
        type=int,
        help="The pooling window size",
        default=POOLING_SIZE)
    parser.add_argument(
        "--kernel_size",
        type=int,
        help="The kernel window size",
        default=KERNEL_SIZE)
    parser.add_argument(
        "--num_filters",
        type=int,
        help="The number of convolutional filters",
        default=NUM_FILTERS)
    parser.add_argument(
        "--num_layers",
        type=int,
        help="Number of convolutional layers",
        default=NUM_LAYERS)
    parser.add_argument(
        "--num_folds",
        type=int,
        help="Number of folds for cross validation",
        default=NUM_FOLDS)
    parser.add_argument(
        "--num_epochs", type=int, default=NUM_EPOCHS, help="Number of epochs")
    parser.add_argument(
        "--img_dimension",
        type=int,
        default=IMG_DIMENSION,
        help="Size of images")
    parser.add_argument(
        "--log",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Logging level")
    args = vars(parser.parse_args())

    # extract logging
    logging.basicConfig(level=args["log"])

    # make sure imgpath exists
    if not Path(args["image_directory"]).is_dir():
        logging.critical("Image Directory does not exist!")
        exit(1)

    if args["num_folds"] < 2:
        logging.critical("There must be 2 or more folds!")
        exit(1)

    return args