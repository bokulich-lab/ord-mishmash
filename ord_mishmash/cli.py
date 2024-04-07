"""
The command-line interface for the PyScraper
"""

import argparse
from .metadatafetcher import get_metadata
from .scrape_pdf import pdf_analysis
import nltk

def installNltkPunktDataSet():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')


def main():
    installNltkPunktDataSet()

    parser = argparse.ArgumentParser(
        description="Python package to evaluate biomedical scietific study papers"
    )
    parser.add_argument('command', choices=['get_metadata','pdf_analysis'])
    parser.add_argument("-e","--email",help = 'user email')
    parser.add_argument("-i",'--accession_ids', nargs='+',dest = 'ids' )
    parser.add_argument('-pmc_ids','--pubmed_central_ids', nargs='+', dest = 'pmc_ids')
    parser.add_argument('-o','--output_file', dest  = 'output')


    
    args = parser.parse_args()
    if args.command == 'get_metadata':
        if not all([args.email,args.ids,args.output ]):       
            parser.error('all parameters -e, -i, -o are required')
        metadata_df = get_metadata(args.email, args.ids)
        print("Result successfully obtained!")
        metadata_df.to_csv(args.output)
        print('Metadata saved to {}'.format(args.output))
    else:
        if not all([args.pmc_ids,args.output]):
            parser.error('all parameters -pmc_ids, -o are required')
        df_analysis = pdf_analysis(args.pmc_ids)    
        print("Result successfully obtained!")
        df_analysis.to_csv(args.output)
        print('Result saved to {}'.format(args.output))
if __name__ == "__main__":
    main()