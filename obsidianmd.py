import re
import os
import shutil


class obsidianMD:
    def __init__(self, inFilepath: str, outFilepath: str):
        self.inFilepath = inFilepath
        self.outFilepath = outFilepath

        self.imagesPath = os.path.join(os.path.dirname(inFilepath), 'images')
        if not os.path.isdir(self.imagesPath):
            self.imagesPath = None

        self.infile = open(self.inFilepath, "r")
        self.outfile = ""
        self.outfileName = ""

        self.subject = ""
        self.subjectPath = ""

        self.properties = {}
        self.__readFrontMatter()

    def __readFrontMatter(self):
        firstline = self.infile.readline()
        if "---" not in firstline:
            self.publish = False
            return

        for line in self.infile:
            if "---" in line:
                break
            else:
                self.properties[line.split(":")[0]] = line.split(":")[1].strip()

    def __writeFrontMatter(self):
        self.outfile.write("---\n")
        self.outfile.write(f"title: {self.subject}\n")
        self.outfile.write(f"weight: {self.properties['weight']}\n")
        self.outfile.write("---\n\n")

    def toPublish(self, lesson: str):
        result = "true" in self.properties["export"] or "True" in self.properties["export"]
        result = result and lesson in self.properties["cours"]
        return result

    def __isLink(self, line: str):
        return "[[" in line

    def __reformatLink(self, line: str):
        link = line[line.find('[[')+2:line.find(']]')]
        insertLink = f"[{link}]({{{{< relref \"{link}\">}}}})"

        linkBeginningPosition = line.find('[[')
        linkEndPosition = line.find(']]') + 2

        newline = line[:linkBeginningPosition] + insertLink + line[linkEndPosition:]
        return newline

    def __isImage(self, line: str):
        return "![[" in line and (".png" in line or
                                  ".jpg" in line or
                                  ".webp" in line)

    def __reformatImage(self, line: str):
        content = line[3:-3].split("|")
        imageName = content[0]

        if len(content) == 1:
            newcontent = imageName
        elif len(content) == 2:
            newcontent = f"{imageName}?width={content[1]}px"

        newline = f"![]({newcontent})\n"

        return newline.replace(" ", ""), imageName

    def __copyImage(self, image):
        imagepath = os.path.join(self.imagesPath, image)
        print(f"copy image: {imagepath} to {self.subjectPath}")
        shutil.copy(imagepath, self.subjectPath)

    def __isCallout(self, line: str):
        return "> [!" in line

    def __reformatCallout(self, line: str):
        calloutType = re.findall('\> \[\!(.*)\]', line)[0]
        newline = f"{{{{%notice style=\"{calloutType}\""
        title = line[line.find("]")+1:].strip()
        if title != "":
            newline = newline + f"title=\"{title}\""
        newline = newline + "%}}\n"
        return newline

    def __createSubjectRelearn(self):
        self.subject = os.path.basename(self.inFilepath)[:-3]
        self.subjectPath = os.path.join(self.outFilepath,
                                        self.properties["path"],
                                        self.subject)
        print(self.subjectPath)
        try:
            os.mkdir(self.subjectPath)
        except FileExistsError as e:
            print(f"Directory {self.subjectPath} already exists: continuing\n")

        self.outfileName = os.path.join(self.subjectPath, "_index.md")

    def reformatFile(self):
        self.__createSubjectRelearn()
        self.outfile = open(self.outfileName, "w")

        self.__writeFrontMatter()

        isInCallout = False
        for line in self.infile:
            if self.__isImage(line):
                line, imageName = self.__reformatImage(line)
                if self.imagesPath is not None:
                    self.__copyImage(imageName)
                else:
                    print(f"Please copy {imageName} file to {self.subjectPath}/")
                    print(f"--> if necessary rename it to {line[4:-2]}\n")

            elif self.__isCallout(line):
                isInCallout = True
                line = self.__reformatCallout(line)

            elif isInCallout:
                if line[0] == ">":
                    line = line[1:]
                # end of callout
                if line.strip() == "":
                    isInCallout = False
                    self.outfile.write("{{% /notice%}}\n")

            elif self.__isLink(line):
                # if multiple link in the same line
                while self.__isLink(line):
                    line = self.__reformatLink(line)

            self.outfile.write(line)

        self.infile.close()
        self.outfile.close()
