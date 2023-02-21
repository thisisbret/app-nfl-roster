I've included a requirements.txt file to easily replicate the environment within conda. Simply run 'conda env create -f requirements.txt'. Even though I've included a copy of the dataset you can get the latest version through the kaggle cli app.

Firstly follow kaggle's instructions for generating your kaggle.json api file, this includes your username and a unique key. You'll store this json file at ~/.kaggle/kaggle.json, replacing the ~ with your home directory path. The cli will automatically look in that location when it runs.

kaggle datasets download bretmontgomery/nfl-roster-2022-season --file nfl-roster-2022-season.parquet --path './assets/datasets/' --force

This command will retrieve the latest version of the file and overwrite the existing one. You'll need to run this command within your conda environment.

Another note to mention; there is a csv version of this dataset hosted on kaggle as well. I've chosen to stick with the parquet filetype for a few reasons. The footprint is significally less, both on disk and in memory. The datatypes are preserved when reading into a pandas DataFrame. Lastly, you're able to specify which columns to read in. Personally, this is easily worth the added dependancy of pyarrow.

pd.read_parquet('path_to_file', columns=['list', 'of', 'columns', 'to', 'include'])

The streamlit app itself should be self explanatory to use. It's very simple to get it running on localhost, simply run this command. It's optional to specify the port as streamlit uses 8501 by default.

streamlit run Home.py --server.port 8501