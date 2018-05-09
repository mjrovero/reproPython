import importlib
import sys

subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

#python src/data/01_subset-data-GBP.py data/raw/winemag-data-130k-v2.csv 
#python src/visualization/02_visualize-wines.py data/interim/2018-05-09-winemag_priceGBP.csv 
#python src/data/03_country-subset.py data/interim/2018-05-09-winemag_priceGBP.csv Chile

if __name__ == '__main__':
    filename = sys.argv[1]
    country = sys.argv[2]
    print('input data filename: {}'.format(filename))
    interim_filename = subset.process_data_GBP(filename)
    print('interim data filename: {}'.format(interim_filename))
    print('creating plots for {}'.format(interim_filename))
    plotwines.create_plots(interim_filename)
    print('analyzing data for country {}'.format(country))
    print(country_sub.get_country(interim_filename, country))
