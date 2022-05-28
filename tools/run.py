import os

TOOLS_ROOT = "/workspaces/antlr4_playground"
ANTLR = "antlr-4.10.1-complete.jar"

# alias grun='java org.antlr.v4.gui.TestRig'

if __name__ == '__main__':
    os.environ['CLASSPATH'] = f".:{TOOLS_ROOT}/{ANTLR}:{os.environ['CLASSPATH']}"
    os.system(f'java -jar {ANTLR}')