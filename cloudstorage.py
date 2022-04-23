import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGQ2kz9rfyV4IHUmFPC5qsopfgedc9ogU_AqCT7cJpaXdJIavS_4w3H2dGHBJ4vncjuZsvrjTQEyHX6ydo45Ol3yJE17pUxmubsUDH-cN2CddrVUhs25jAiHGzRhtD27yJd73LMJMapg'
    transferData = TransferData(access_token)

    file_from = input('Enter the file name transfer ')
    file_to = input("full path to upload to the dropbox ")
    # API v2
    transferData.upload_file(file_from, file_to)
    print("files have been move without any error ")
if __name__ == '__main__':
    main()
