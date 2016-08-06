# See http://dropbox-sdk-python.readthedocs.io/en/master/moduledoc.html#module-dropbox.dropbox

import dropbox
dbx = dropbox.Dropbox('uN8UoPO7BCoAAAAAAAAKtANTnRKzUuKymvAreaS90O90kiXaQoQrZPWDxJFd2UOO')
try:
    dbx.files_upload("Hello, this is a text", '/text.txt', dropbox.files.WriteMode('overwrite', None))
except dropbox.exceptions.ApiError as err:
    print("Error uploading file:" , err)