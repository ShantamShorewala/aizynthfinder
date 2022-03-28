from aizynthfinder.aizynthfinder import AiZynthFinder

def main():

	config_filename = 'config.yml'
	finder = AiZynthFinder(configfile = config_filename)

	finder.stock.select("zinc")
	finder.expansion_policy.select()
	finder.filter_policy.select()

	

main()