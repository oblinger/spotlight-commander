

<h4>
UNIFORM provides for SOURCE-CODE what <br>
YAML provides for LISTS:
</h4>

A human enjoyable "obvious" syntax <br>
which maps in the obvious way onto JSON.


#### Like YAML, UNIFORM is:

* **LOSSLESS** -- Any source structure printed into Uniform is guaranteed to parse back into a structure EQUAL to the original.

* **PURELY SYNTACTIC** -- Uniform parses a generic C/Java/Python/Scala-ish language in a purely-syntactic way onto JSON.  (e.g. no special parsing is done for speciali forms like "while" or "if")
  
* **MARKDOWN-ish** -- Like both markdown and YAML, Uniform has constructs optimized to look simple and beautiful in their UNICODE source format.
  
* **OBVIOUS** -- Like YAML, Uniform is "obvious".  Without reading docs, an engineer can view 'uniform' source then know what it means and what JSON structure it maps to.

* **VARIATIONAL** -- Like YAML, Uniform provides multiple alternate surface forms which aid readability for specific common cases.

* **UNIFORM** -- Like YAML, Uniform maps all that surface variation onto a simple uniform JSON structure which aids in simple machine processing.

Thus Uniform is a bridge for code like structures which allows humans to view and edit in format optomized for them, and ALSO allowing machines to process the same structures in a bridged form opotmize for machine processing.



## So what is the UNI-FORM?

```python
    head(VALUE1, VALUE2, ..., key_a: VALUE_A, key_b: VALUE_B, ...)     
```

The entire __Uniform Language__ maps onto recursive applications of the single "uni"-form above.  As you can see the uni-form looks like a standard function call from any procedural language -- it names the function called, a sequence of fixed arguments, followed by a set of keyword argument.  This same uni-form also maps trivially into the JSON object as shown here:

```javascript
     {'^':'head', '^1':VALUE1, '^2':VALUE2,  'key_a':VALUE_A, 'key_b:VALUE_B}
```

In uniform, values can either be a sub-"uni"-form expressions, or one of the  JSON constant values:  null, true, false, __a string__, or __a number__.  This defines the entire Uniform langauge! 

Because Uniform is a slightly simplified verions of JSON, it is trivial to map between them.  Two special head values are used:  'object', and 'list'.  object( ... ) is the "uni"-form for a JSON object that does not have any head ("^") key, and list( ... ) is the "uni"-form representation of a JSON list [ ... ].  





## Uniform syntax

As described, there are a number of alternate surface forms for the "uni"-form.
Each of these alternate forms bi-directionally map losslessly onto the "uni"-form itself.
So the viewer should just remember, in all cases these very different surface forms all
map down to the obvious recursive expression of procedural function calls with fixed and keyord parameters.


    -:- First a motivating example showing a number of the alternate surface forms in the uniform language.
    ::Person
        name := 'Dan Oblinger
		funky_string := 'like YAML, string do not need back quoting.  even 
		                 multi-line strings with "quotes" and 'quotes' and back quotes \ are just fine.
        home :: Address '3403 Cesar Chavez   Apt := C                 -:- Indention can be used to indicate the end of an embedded object
                         City := San Francisco   State := CA   zip := 94110
        email := 'dan@oblinger.us
        friends := 'Qingling Ni ,: 'Jack Porter ,: 'Josh Yelon ,:
            ::Person  name:='Inline-defined Person                    -:- Notice this fourth friend is actually an in-line defined object
                      home::Address 1234 inline street address 
    		                City:=Some City  State:=CA  Zip:=12345
    
        theorems::
            a^2+b^2 == c^2                              -:- This is not a string, it is a recursive uniform code expression with inline operators
			                                            -:- Modern procedural lanaguage differ on which infix operators they include, but all lanaguage agree
														-:- on the PRECIDENCE between these operators...  so we have just included them ALL in Uniform
    
        good_old_JSON_still_works_here::
            {"equation": ["equals", "e", ["times" "m" ["squared", "c"]]]}       -:- Like YAML, Uniform is a superset of JSON
    
        some_uniform_code::
            def factorial(x) {
    	        if x<=1 { 
    	            return 1
    	        } else { 
    	            return x * factorial(x-1)
    	        }
            }
    
        some_embedded_source_code:: java                -:- Notice here we are embedding the source code of another language 
                                                        -:- and we do NOT need to add any backquoting !!
    	    import java.lang;
                package com.my.package;
    	    public static final EmbeddedMethodDefinition(String arg1, int arg2) { 
    	         system.out.println("Just a bit of Java here")
            }
    
    
            
As you can see from the example above, there are a few alternate
notations added to the uniform language beyond those found in
C/Java/Python.  These forms are still just syntactic sugar providing
alternative representations of the uni-form which are helpful for
encoding certain complex source material.  But importantly, all of
these alternative forms simply aid in human-readability, the
resulting data structures are always nothing more than a recursive application of the UNI-form.

Appendix A provides a formal specification of Uniform and of each of the
surface forms shown.  Here we simply demonstrate by example, showing the alternative form,
followed by its uni-form, and JSON equivelants.  In each case, all threee expressions are __valid uniform__
and all three map to the same underlying JSON:

<br><br>

|                    | **PREFIX / INFIX OPERATORS** |
| ------------------ | ---------------------------- |
| Format             | __expr__ **OP** __expr__     |
| Examples           | - some_var <br> x^2+y^2      | 
|  as uni-form       | "+"( "^"(x, 2), "^"(y, 2) )  |
|  as a JSON         | {"^":"+", "^1": {"^":"^", "^1":"x", "^2":2}, {"^":"^", "^1":"y", "^2":2} } |

The Uniform Language includes all of the prefix and infix operators that exist in Java, C, Python, Ruby, and many from C++.

<br><br>


|                    | **STATEMENT FORMS**         |                                        |
| ------------------ | --------------------------- | -------------------------------------- |
| Format             | __head__ __arg1__ ... **;** |  __head__ __arg1__ ... **{** ... **}** |
| Examples           | print "Hello World!";       |  while x>0 { x-=1 }                    |
|  as uni-form       | print("Hello World!")       |  while( '>'(x,0), '-='(x,1) )          |
|  as a JSON         | {"^":"print", "^1": "'Hello World!"} | while( '>'(x,0), '-='(x,1) )  |

A statement is just like a uniform expression except it does not have parens, instead it ends with a semicolon (' **;** '),
or it ends with a block form **{** ... **}**.

<BR><br>


|                   | **BLOCK FORM**                                           | 
| ----------------- | -------------------------------------------------------- |
| Format            | **{** stmt1 stmt2 ... **}**                              |
| Alternate form:   | { str = "looks like C code to me!"; print str }          |
|  as uni-form      | block( "="(str, "looks like C code to me!"), print(str)) |
|  as a JSON        | {"^":"block", "^1": {"^":"=", "^1":"str", "^2":"'looks like C code to me!"}, {"^":"print", "^1":"str"} } |

Blocks are simply sequences of the statement forms as shown above.  Statements and blocks can be put together into complex structures that closely match common procedural idioms.  To show how natural and how flexible the block/statement parsing can be we provide this Uniform example followed by its uni-form equivelant:

```
def nonsense_fn(x, int y, z=5) {
	with open("out.txt", mode:read) as x {
		x,y = y,x
	}
}
```

```
def( nonsense_fn(x, int(y), '='(z, 5)), block( 
	with( open("out.txt", mode="r"), as, x, block(
		'='( ','(x, y), ','(y,x) )  ))  ))
```

As with all uni-forms, this latter form trivially maps to JSON as well, of course because JSON is such a poor format for code-like structures, we will not force the reader to endure that uninteligable mess!  Still a source-code processing algorithms will have no issue with this JSON, indeed JSON is perhaps the most elegant format for machine processing of source-code structures.

Indeed this is the beauty of Uniform:
(1) Its parsing is universal -- it does not depend upon knowing which keywords like 'int' or 'def' are special for your language, its translation is purely syntactic, just as the parsing of homoiconic languages like LISP are purely syntactic.  So it is extensible and self manipulatable as only homoiconic languages can be.
(2) Its source form is expressed in the C/Java/Python way that most modern programmers find most natural.
(3) Its parse form is expressed in JSON -- the simplest, most widespread machine processible representation.

This hat-trick allows Uniform to provide the best of all worlds: the best form for humans, the best form for machine, and a universal, purely-syntacti, bi-directional, lossless mapping which allows programmers to extend and invent new langauge constructs that continue to look good on the human side, continue to be trival to process on the machine side, and does not require them to mess with or alter the parsing/printing infrastructure at all!

The Uniform Langauge brings the advantages of homoiconicity to good old fashion procedural langauges w/o costing any of the readability typically associated with such languages.




<br><br>

## Other Uniform extensions


|                    | **COLON FORMS**              |
| ------------------ | ---------------------------- |
| Formats            | **{:** __key1__ **:=** __val1__ **,:**  ... **:}** <br> **[:** __val1__ **,:** ... **:]** <br> __head__ **(:**  __val1__ **,:** ... **,:** __key_a__ **:=** __val_a__ **,:**  ... **:)** <br> **'** some string |
| Examples           | {: key:='some value  then:=another(: 'value :) <br> &nbsp; &nbsp; a_list :== [: 'list ,: 'of values :] <br> some_function(: key:= val :)  :}  | 
|  as uni-form       | object( key: "some value", then: another("value"), a_list: ["list", "of values"] ) |

Uniform is designed to embed one source language into the fields of another.  These colon forms facilitate implicitly terminated strings (the **'** operator) which generally do not require escaping **"** or other syntax, since the colon forms themselves rarely occur within the source code of other languages.  (In those rare exceptional cases, a traditional backslash can still be used.)



WHITESPACE SENSITIVE BLOCK FORM 

|                  | **WHITESPACE SENSITIVE BLOCK FORM**
| ---------------- | ---------------------------------------------------------------------------------- |
| Format           | **::** __head__ <br> &nbsp; &nbsp; &nbsp; &nbsp; ... <br> __key__ **::** __head__ <br>  &nbsp; &nbsp; &nbsp; &nbsp; ... |
| Examples         | ::Person <br> &nbsp; home :: Address 111 Maple lane  zip:=12345                    |
 |   as uni-form:   |    Person( home=Address( "111 Maple lane", zip=12345 ) )                           |
|   as a JSON:     |    {"^":"Person", "home" : {"^":"Address", "^1":"111 Maple lane",  "zip":12345 } } |

The **::** form is the only whitespace sensitive form in the Uniform language.  This allows creation of deeply structured JSON objects without the nearly-impossible-to-diagnose errors from misaligned closing braces. (Modern editors detect mis-matched braces, but can provide no help if braces are balanced by do not convey the nesting expected by the user.)


COLON FORMS

SYMBOL FORM








# Appendix B

The careful reader might note some odd translations in the uni-form above, for example ' int(y) ' looks like we are passing y to some function called int.  Of course declaring a variable in any modern procedural language cannot be implemented by passing the variable to the "int-ifier" function.  But that is not the point here 

Certain forms (for example the if-elif-elif-else form requires some post processing, but as Appendix B shows, even that form fits into Uniform.  






##### STATEMNT FORM

| equivelant forms | **STATEMENT FORMS** |
| ---------------- | ------------------- |
| Alternate form:  | x^2+y^2               | 
|  as uni-form      | "+"( "^"(x, 2), "^"(y, 2) ) |
|  as a JSON        | {"^":"+", "^1": {"^":"^", "^1":"x", "^2":2}, {"^":"^", "^1":"y", "^2":2} } |





	Alternate form:       if x==y then:
	                          return "Same"
    	                  else:
						      return "Different"
    	                  end

    as uni-form:          if( equal(x, y), then=return("Same"), else=return("Different"))
	
	as a JSON form:       {"^":"if", "^1": {"^":"equals", "^1":"x", "^2":"y"},
                               "then": {"^":"return", "^1":"Same"},
						       "else": {"^":"return", "^1":"Different"} }
.

    Alternate form:       java_source := 'system.out.println("embedded \"quotes\" and backquotes (\\) are a needless pain!");
	as a JSON form:       { "java_source": "system.out.println(\"embedded \\\"quotes\\\" and backquotes (\\\\) are a needless pain!\");", 




# OLD

##The UNI-FORM syntax

Uniform encodes the disparate informational forms 
spanning modern "source code" languages in a single common syntax.
The aim is to be as human readable when encoded in uniform as it was
in its original forms, AND, simultaneously be easily machine readable,
writable, and editable.  Uniform is to source code, what YAML is to lists 
and maps -- a schema-less, human-pleasing, universal, loss-less, 
bi-directionally mapped syntax.





## UNIFORM REPRESENTATION

Uniform is a homo-iconic language.  This means its source code maps
into its data structure just as the Lisp language does.  But unlike
Lisp, uniform uses the familiar C/Java/Python expression syntax,
instead of the non-standard (and hard-to-read) parenthesis notation of
Lisp.  Further Uniform's underlying data-structure is the extremely
prevalent JSON object form whereas Lisp is built on the less commonly
used sexpr data structure.

At the bottom, all uniform source-code maps to a recursive application 
of the "UNI"-form itself.  The simplest presentation of the uni-form 
looks like a Python function call with keyword arguments.  The uni-form:

    head(VALUE1, VALUE2, ..., key_a=VALUE_A, key_b=VALUE_B, ...)     

The uni-form also maps trivially onto the JSON object notation:
   
     {'^':'head', '^1':VALUE1, '^2':VALUE2,  'key_a':VALUE_A, 'key_b:VALUE_B}

In uniform, values can either be a sub-uniform expression, or a JSON constant value like a string or number.  That's it.  That is the uni-form data structure.

##  xxx




## UNIFORM REPRESENTATION

Uniform is a homo-iconic language.  This means its source code maps
into its data structure just as the Lisp language does.  But unlike
Lisp, uniform uses the familiar C/Java/Python expression syntax,
instead of the non-standard (and hard-to-read) parenthesis notation of
Lisp.  Further Uniform's underlying data-structure is the extremely
prevalent JSON object form whereas Lisp is built on the less commonly
used sexpr data structure.

At the bottom, all uniform source-code maps to a recursive application 
of the "UNI"-form itself.  The simplest presentation of the uni-form 
looks like a Python function call with keyword arguments.  The uni-form:

    head(VALUE1, VALUE2, ..., key_a=VALUE_A, key_b=VALUE_B, ...)     

The uni-form also maps trivially onto the JSON object notation:
   
     {'^':'head', '^1':VALUE1, '^2':VALUE2,  'key_a':VALUE_A, 'key_b:VALUE_B}

In uniform, values can either be a sub-uniform expression, or a JSON constant value like a string or number.  That's it.  That is the uni-form data structure.


----

|                    | **STATEMENT FORMS**         |
| ------------------ | --------------------------- |
| Examples           | while x>0 { x-=1 }       |
|  as uni-form       | while( '>'(x,0), '-='(x,1) ) |
|  as a JSON         | {"^":"print", "^1": "'Hello World!"} |

Or a statement is ended by the FIRST **{** ... **}** form found.


<br><br>

# end
---
Copyright (c)  Daniel Oblinger
