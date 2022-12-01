import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="DENS")

    # ===== dataset ===== #
    parser.add_argument("--dataset", nargs="?", default="beauty",
                        help="Choose a dataset:[baby,beauty,home,toy,lastfm]")
    parser.add_argument(
        "--data_path", nargs="?", default="data/", help="Input data path."
    )

    # ===== train ===== # 
    parser.add_argument("--gnn", nargs="?", default="lightgcn",
                        help="Choose a recommender:[lightgcn]")
    parser.add_argument('--epoch', type=int, default=1000, help='number of epochs')
    parser.add_argument('--batch_size', type=int, default=2048, help='batch size')
    parser.add_argument('--test_batch_size', type=int, default=2048, help='batch size in evaluation phase')
    parser.add_argument('--dim', type=int, default=64, help='embedding size')
    parser.add_argument('--l2', type=float, default=1e-4, help='l2 regularization weight, 1e-5 for NGCF')
    parser.add_argument('--lr', type=float, default=1e-3, help='learning rate')
    parser.add_argument("--mess_dropout", type=bool, default=False, help="consider mess dropout or not")
    parser.add_argument("--mess_dropout_rate", type=float, default=0.1, help="ratio of mess dropout")
    parser.add_argument("--edge_dropout", type=bool, default=False, help="consider edge dropout or not")
    parser.add_argument("--edge_dropout_rate", type=float, default=0.1, help="ratio of edge sampling")
    parser.add_argument("--batch_test_flag", type=bool, default=True, help="use gpu or not")

    parser.add_argument("--ns", type=str, default='dens', help="rns,dns,dens,mix")
    parser.add_argument("--K", type=int, default=1, help="number of negative in K-pair loss")
    parser.add_argument("--alpha", type=float, default=1, help="weight for relevant factor")
    parser.add_argument("--warmup", type=float, default=100, help="weight for relevant factor")
    parser.add_argument("--gamma", type=float, default=0.3, help="weight for gating task")

    parser.add_argument("--n_negs", type=int, default=6, help="number of candidate negative")
    parser.add_argument("--pool", type=str, default='mean', help="[concat, mean, sum, final]")

    parser.add_argument("--cuda", type=bool, default=True, help="use gpu or not")
    parser.add_argument("--gpu_id", type=int, default=1, help="gpu id")
    parser.add_argument('--Ks', nargs='?', default='[20]',
                        help='Output sizes of every layer')
    parser.add_argument('--test_flag', nargs='?', default='part',
                        help='Specify the test type from {part, full}, indicating whether the reference is done in mini-batch')

    parser.add_argument("--context_hops", type=int, default=3, help="hop")

    # ===== save model ===== #
    parser.add_argument("--save", type=bool, default=False, help="save model or not")
    parser.add_argument(
        "--out_dir", type=str, default="./weights/beauty/", help="output directory for model"
    )

    return parser.parse_args(args=[])
