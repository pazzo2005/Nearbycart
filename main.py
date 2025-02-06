

from process_data import combine_data
from store_data import save_to_csv

if __name__ == "__main__":
   
    combined_data = combine_data()

   
    save_to_csv(combined_data)
