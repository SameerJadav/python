filename = input("File name: ").lower().strip()

#images
if ".gif" in filename:
    print("image/gif")
elif ".jpg" in filename or ".jpeg" in filename:
    print("image/jpeg")
elif ".png" in filename:
    print("image/png")
#application
elif ".pdf" in filename:
    print("application/pdf")
elif ".zip" in filename:
    print("application/zip")
#text
elif ".txt" in filename:
    print("text/plain")
#anything else
else:
    print("application/octet-stream")