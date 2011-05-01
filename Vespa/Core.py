from subprocess import call

def callTheDemon(vessel):
        invocation = "./vespa \"{args}\"".format(args=collectTheBlood(vessel))
        exitCode = call(invocation, shell=True)
        return exitCode

def collectTheBlood(vessel):
        return ()

