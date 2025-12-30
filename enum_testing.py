from enum import IntFlag


class MsiInstallState(IntFlag):
    msiInstallStateNotUsed = -7
    msiInstallStateBadConfig = -6
    msiInstallStateIncomplete = -5
    msiInstallStateSourceAbsent = -4
    msiInstallStateInvalidArg = -2
    msiInstallStateUnknown = -1
    msiInstallStateBroken = 0
    msiInstallStateAdvertised = 1
    msiInstallStateRemoved = 1
    msiInstallStateAbsent = 2
    msiInstallStateLocal = 3
    msiInstallStateSource = 4
    msiInstallStateDefault = 5


if __name__ == "__main__":
    print((repr(MsiInstallState.msiInstallStateUnknown), MsiInstallState.msiInstallStateUnknown.value))
    assert MsiInstallState.msiInstallStateUnknown == -1
