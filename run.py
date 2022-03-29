from aizynthfinder.aizynthfinder import AiZynthFinder
import argparse

def get_args():

	parser = argparse.ArgumentParser()
	parser.add_argument('--configfile', type=str, required=True, default='config_neuralsim')
	parser.add_argument('--finder', type=str, required=False, default='zinc')
	parser.add_argument('--policy', type=str, required=False, default='my_policy')
	parser.add_argument('--targets', type=str, required=False, default='data/targets/retrostar190.txt')

	args = parser.parse_args()
	return args

def main():

	args = get_args()

    # config_filename = 'config_neuralsim.yaml'
    finder = AiZynthFinder(configfile = args.configfile)

    finder.stock.select(args.finder)
    finder.expansion_policy.select(args.policy)
    #finder.filter_policy.select()

    with open(args.targets, 'r') as f:
    	for row in f:
	    finder.target_smiles = row#"Cc1cccc(c1N(CC(=O)Nc2ccc(cc2)c3ncon3)C(=O)C4CCS(=O)(=O)CC4)C"
	    finder.tree_search()

	    finder.build_routes()
	    stats = finder.extract_statistics()
	    print (stats, "\n")

main()
