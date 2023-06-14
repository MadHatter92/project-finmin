import requests
import os

url_base= "https://www.indiabudget.gov.in/doc/bspeech/"

start_year = 1947
end_year = 2022

fy_begin = start_year
destination_folder = "./Budget_Speeches_PDF/"

def download_pdf(url, destination_folder):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the file name from the url
        filename = url.split("/")[-1]
        # Create the full path for the destination
        destination_path = os.path.join(destination_folder, filename)
        
        with open(destination_path, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {filename} into {destination_folder}')
    else:
        print('Failed to download file')

while fy_begin != end_year+1:
	fy_end = fy_begin+1
	stub = "bs"+str(fy_begin)+str(fy_end)[-2]+str(fy_end)[-1]
	url = url_base+stub+".pdf"
	print(url)
	download_pdf(url, destination_folder)
	fy_begin = fy_begin + 1