
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BIfSHOThNvjfAKC3flyBpn0zKufCeaO_eaP1zHEblh6VMUpSbRIBK1bVHoQ-pv0ibSGuDKX_ILvPYl9GAAY4VHpZvT3eB_KNIZ947WXSpSzR4qr_IThONH3qtyGnEiyDWJyfnhI'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()