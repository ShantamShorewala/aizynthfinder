from aizynthfinder.aizynthfinder import AiZynthFinder

def main():

        config_filename = 'config_neuralsim.yaml'
        finder = AiZynthFinder(configfile = config_filename)

        finder.stock.select("zinc")
        finder.expansion_policy.select("my_policy")
        #finder.filter_policy.select()

        finder.target_smiles = "Cc1cccc(c1N(CC(=O)Nc2ccc(cc2)c3ncon3)C(=O)C4CCS(=O)(=O)CC4)C"
        finder.tree_search()

        finder.build_routes()
        stats = finder.extract_statistics()
        print (stats)
test
main()
