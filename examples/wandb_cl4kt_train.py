import argparse
from wandb_train import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #train config
    parser.add_argument("--dataset_name", type=str, default="assist2009")
    parser.add_argument("--model_name", type=str, default="cl4kt")
    parser.add_argument("--emb_type", type=str, default="qid")
    parser.add_argument("--save_dir", type=str, default="saved_model")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--fold", type=int, default=0)
    
    parser.add_argument("--use_wandb", type=int, default=1)
    parser.add_argument("--add_uuid", type=int, default=1)
    
    #model config
    parser.add_argument("--hidden_size", type=int, default=256)
    parser.add_argument("--num_blocks", type=int, default=2)
    parser.add_argument("--num_attn_heads", type=int, default=4)
    parser.add_argument("--kq_same", type=int, default=1)
    parser.add_argument("--final_fc_dim", type=int, default=256)
    parser.add_argument("--final_fc_dim2", type=int, default=256)
    
    parser.add_argument("--d_ff", type=int, default=256)
    parser.add_argument("--dropout", type=float, default=0.1, help="dropout probability")
    parser.add_argument("--reg_cl",type=float,default=1,help="regularization parameter contrastive learning loss")
    parser.add_argument("--mask_prob", type=float, default=0.5, help="mask probability")
    parser.add_argument("--crop_prob", type=float, default=0, help="crop probability")
    parser.add_argument("--permute_prob", type=float, default=0, help="permute probability")
    parser.add_argument("--replace_prob", type=float, default=0, help="replace probability")
    parser.add_argument("--negative_prob",type=float,default=0,help="reverse responses probability for hard negative pairs")
    parser.add_argument("--temp", type=float, default=1)
    parser.add_argument("--hard_negative_weight", type=float, default=1)
    parser.add_argument("--learning_rate", type=float, default=1e-4)
    parser.add_argument("--cl_emb_use_pos", type=int, default=0, help="use position embedding for contrastive learning")
    parser.add_argument("--random_action", type=int, default=-1, help="randomly choose actions for data augmentation")
    
    args = parser.parse_args()
    
    params = vars(args)
    main(params)
