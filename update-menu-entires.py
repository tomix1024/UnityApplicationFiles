import os
import glob

HomePath = os.path.expanduser("~")

UnityBasePath = '/opt/Unity'
ApplicationsPath = os.path.join(HomePath, '.local/share/applications')

UnityVersionNames = [ Dir for Dir in os.listdir(UnityBasePath) if os.path.isdir(os.path.join(UnityBasePath, Dir)) ]
TemplateApplicationFiles = [ File for File in os.listdir('.') if File.endswith(".desktop") ]


# Clean existing application files
for TemplateApplicationFile in TemplateApplicationFiles:

    SearchPath = os.path.join(ApplicationsPath, TemplateApplicationFile.replace('UNITY_VERSION', '*'))
    for File in glob.glob(SearchPath):
        print("remove file " + File)
        os.rename(File, File + '.bak')

# Create new application files
for TemplateApplicationFile in TemplateApplicationFiles:

    for UnityVersionName in UnityVersionNames:
        ApplicationFile = TemplateApplicationFile.replace('UNITY_VERSION', UnityVersionName)
        print("create file " + ApplicationFile)

        with open(TemplateApplicationFile, "rt") as InputFile:
            with open(os.path.join(ApplicationsPath, ApplicationFile), "wt") as OutputFile:
                for Line in InputFile:
                    OutputFile.write(Line.replace('UNITY_VERSION', UnityVersionName))
