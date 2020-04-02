class File:
    def writeToFile(self, text, file):
        file = open('a')
        file.write(str(round(text, 3)))
        file.close()