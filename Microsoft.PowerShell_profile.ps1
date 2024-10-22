## Color
$PSStyle.FileInfo.Directory = "`e[36m"
$PSStyle.FileInfo.Executable = "`e[91m"

## Encoding
[Console]::OutputEncoding = [System.Text.Encoding]::GetEncoding('utf-8')
$OutputEncoding = [Text.Encoding]::Default

## Console
$prompt_default = "$([char]27)[0m";
$prompt_bright_red = "$([char]27)[91m";
$prompt_bright_blue = "$([char]27)[94m";
$new_line = "$([char]10)";
function prompt() {
    $isRoot = (([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
    $prompt_color = if ($isRoot) {$prompt_bright_red} else {$prompt_bright_blue};
    "$new_line$prompt_color┌──($prompt_default$($executionContext.SessionState.Path.CurrentLocation)$prompt_color)$new_line" + "└─$('<' * ($nestedPromptLevel + 1)) $prompt_default";
}
## PS> (Get-Item function:prompt).Definition
## "PS $($executionContext.SessionState.Path.CurrentLocation)$('>' * ($nestedPromptLevel + 1)) ";
## # .Link
## # https://go.microsoft.com/fwlink/?LinkID=225750
## # .ExternalHelp System.Management.Automation.dll-help.xml

# ## Key Handler
# Set-PSReadLineKeyHandler -Chord Ctrl+a -Function BeginningOfLine
# Set-PSReadLineKeyHandler -Chord Ctrl+e -Function EndOfLine
# Set-PSReadLineKeyHandler -Chord Ctrl+w -Function BackwardKillWord
# # Set-PSReadLineKeyHandler -Chord Ctrl+Delete -Function KillWord
# Set-PSReadLineKeyHandler -Chord Ctrl+u -Function BackwardDeleteLine
# Set-PSReadLineKeyHandler -Chord Ctrl+k -Function ForwardDeleteLine

## Alias (function)
function la() {
    ls -Force $args[0]
}

function weather() {
    curl "https://wttr.in"
}

# function file() {
#     $bash_command = "file $($args[0])" -replace "\\", "/"
#     bash -c $bash_command
# }

# function args_test() {
#     echo $args.Length
#     echo "$($args): $($args.GetType().Name)"
#     If ($args.Length -ne 0) {
#         echo "$($args[0]): $($args[0].GetType().Name)"
#         echo "$($args[0][0]): $($args[0][0].GetType().Name)"
#     }
# }

Set-Alias sakura 'c:\Program Files (x86)\sakura\sakura.exe'