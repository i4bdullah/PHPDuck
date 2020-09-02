# PHPDuck

PHPDuck is a non-alphanumeric PHP code encoder, it uses only the following ten special characters: \[]()$_;+.=  
It was originally created to solve a CTF challenge that allowed users to pass certain set of special characters to eval(), it could be useful to bypass some WAFs too.

# Usage
Tip: Make your code as simple as possible
```
Usage: python3 PHPDuck.py "<PHP CODE>"
Example: python3 PHPDuck.py "system('id');"
Example: python3 PHPDuck.py "readfile('config.php');"
```

## Limitations
* Do not support numbers encoding
* Do not support encodinng of any special character other than: \[]()$_;+.=

### TODOs

 - Numbers support
 - More special characters support
 - Improve error handling

