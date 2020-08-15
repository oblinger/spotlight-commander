
=== OLD ===


<h4>
UNIFORM provides for SOURCE-CODE what <br>
YAML provides for LISTS:
</h4>
A human enjoyable "obvious" format which maps onto JSON an obvious way.


<br><br> 

YAML allows one to quickly implement new data formats that are both easily authored and understood by humans, AND
easy to machine process.  In a similar way, UNIFORM allows one to quickly implement new code-like languages that are
likewise easily authored, understood, and machine processed.



#### Like YAML, UNIFORM is:

* **LOSSLESS** -- Any source structure printed into Uniform is guaranteed to parse back onto a JSON structure 
  EQUAL to its original.

* **BI-DIRECTIONAL** -- Uniform expressions map losslessly onto JSON, and conversely JSON expressions also map losslessly 
  onto Uniform.  (Indeed bi-directional, lossless mappings exists for many common formats:  
  JSON, RDF, Lisp sexprs, etc.)

* **PURELY SYNTACTIC** -- Uniform parses a generic C/Java/Python/Scala-ish language in a langauge-independent, 
  purely-syntactic way onto JSON.  (e.g. this means no specialized parsing is required for language special 
  forms like "while", "if", "class", etc.)
  
* **MARKDOWN-ish** -- Like both markdown and YAML, Uniform first priority is to have its constructs optimized to 
  look simple, intuitive, and beautiful in their textual form.
  
* **OBVIOUS** -- Like YAML, Uniform is "obvious".  By viewing a handful of examples, an engineer already familiar
  with modern programming languages, can infer the JSON mappings for complex uniform sourcecode, without 
  need for reference documentation.

* **VARIATIONAL** -- Like YAML, Uniform provides multiple alternate surface forms which the author can use
  to aid readability in specific common cases.

* **UNIFORM** -- Like YAML, Uniform maps all that surface variation onto simple underlying data structures 
  (JSON) optimized for machine processing.


Thus Uniform is a generic bridge to source-code like info, just as YAML is a generic bridge to data-structure like info.



## So what is the "uni"-form?

The entire Uniform Language is nothing more than recursive applications of this single _"uni"_-form shown here:  

```python
    HEAD(VALUE_, _VALUE_2, ..., key_a: VALUE_A, key_b: VALUE_B, ...)     
```

As you can see the uni-form looks like a standard function call from any procedural language.
It has a "head" -- the function being "called", a sequence of fixed arguments, followed by a set of keyword arguments.  

The "uni"-form maps trivially onto JSON as shown here:

```javascript
     {'^':'head', '^1':VALUE_1, '^2':VALUE_2,  'key_a':VALUE_A, 'key_b:VALUE_B}
```

Each value in uniform can either be a sub-"uni"-form expressions, a _string_, a _number_, or one of the  
JSON constants: null, true, false.  This defines the entire Uniform language!





## Variational Forms

The "uni"-form format above is called _Canonical Uniform_.   For any Uniform expression it has exactly one 
canonical form.  Like YAML, we include multiple surface forms in order that common types of data each have 
natural and beautiful textual forms.  In considering the example below, keep in mind **_ALL_** of these surface
forms map losslessly down to Canonical Uniform above in the obvious way:

    # Here is a motivating example showing the wide range of alternate surface forms possible in Uniform.
    ::Person
        name: 'Dan Oblinger
        # Indention can be used to indicate the end of an embedded object
		funky string: 'like YAML, string do not need back quoting.  even 
		               multi-line strings with "quotes" and 'quotes' and back quotes \ are just fine.
        home :: Address '3403 Cesar Chavez street
            Apt  : C            
            City : San Francisco   
            State: CA   
            zip  : 94110
        email: 'dan@oblinger.us
        friends: ["Qingling Ni", "Jack Porter", "Josh Yelon",
            ::Person  name:='Inline-defined Person                    -:- Notice this fourth friend is actually an in-line defined object
                      home::Address 1234 inline street address 
    		            City:Some City  
    		            State:CA  
    		            Zip:12345
        ]
        good old JSON still works here:
            {"equation": ["equals", "e", ["times" "m" ["squared", "c"]]]}       -:- Like YAML, Uniform is a superset of JSON
 
         theorems:
            a**2 + b**2 == c**2                         -:- This is not a string, it is a recursive uniform code expression with inline operators
			                                            -:- Modern procedural lanaguage differ on which infix operators they include, but all lanaguage agree
														-:- on the PRECIDENCE between these operators...  so we have just included them ALL in Uniform
    
   
        some_uniform_code_that_looks_like_C_or_Java:
            {
                def factorial(x) {
        	        if x<=1 { return 1; }
    	            else { return x * factorial(x-1); }
                }
            }
        
        the_same_uniform_expression_expressed_in_pythonish_way:::
            def factorial(x):
                if x<=1:
                    return 1
                else:
                    return x * factorial(x-1
        
        
        some_embedded_source_code:: .java          # Notice here we are embedding the source code of another language 
                                                   # and we do NOT need to add any backquoting !!
    	    import java.lang;
                package com.my.package;
    	    public static final EmbeddedMethodDefinition(String arg1, int arg2) { 
    	         system.out.println("Just a bit of Java here")
            }
    
    
            
As you can see from the example above, there are YAML-like alternate
notation added to Uniform to aid in visually organizing structured or record-like data, and code-like notations for
presenting mathematical or execution expressions.  But in all cases, this diversity of surface form are just syntactic 
sugar providing alternative representations of the underlying singular uni-form, but each alternative is helpful for
encoding certain common complex source data.  

 # But importantly, all of
 # these alternative forms simply aid in human-readability, the
 # resulting data structures are always nothing more than a recursive application of the UNI-form.

Appendix A provides a formal specification of Uniform and of each of the
surface forms shown.  Here we simply demonstrate by example, showing each alternative form,
followed by its uni-form, and JSON equivalents.  In each case, all three expressions are __valid uniform__
and all three are parsable by Uniform onto the same underlying JSON:


<h4> Brace Forms

The fixed and keyword arguments in the body of the uni-form are flexible enough to capture many non-function call 
constructs that occur in other languages.  
 
 To enable this we allow the same fixed-arguments / keyword-arguments form inside of all brace pairs,  
 \{ ... \} and \[ ... \] as we already allow in the uniform \( ... \) pairs, and we allow the head of the uni-form
 to either be dropped, or to be an entire uniform expression rather than simple a symbol.
 
 To distinguish between these three brace types in both their prefix and infix format we end up with six variants 
 that all map down onto simple uni-form equivalents:
 
 
|                   |   Example Form             | Uniform Variational Form                   |  Canonical Uni-form Equivalent         |
| ----------------- | -------------------------- | ------------------------------------------ | -------------------------------------- |
| '[' prefix form   |  [1,2,3]                   | **[** _arg1_ **,** _arg2_ **,** ... **]**  | **List**(  _arg1_ , _arg2_ , ... )     |
| '[' infix form    |  my_array[5]               | _BASE_ **[** _arg1_ **,** ... **]**        | **ref**(   _BASE_ , _arg1_ , ... )     |
| '(' prefix form   |  (1, 2, 3)                 | **(** _arg1_ **,** _arg2_ **,** ... **)**  | **Tuple**( _arg1_ , _arg2_ , ... )     |
| '(' infix form    |  fn(1, 2)                  | _BASE_ **(** _arg1_ **,** ... **)**        | **call**(  _BASE_ , _arg1_ , ... )     |
| '{' prefix form   |  {"dan", zipcode:"94110"}  | **{** _arg1_ **,** _arg2_ **,** ... **}**  | **Object**( _arg1_ , _arg2_ , ... )    |
| '{' infix form    |  if true { print("this") } | ... **{** _arg1_ **,** ... **}**           | **Block**(  _arg1_ , _arg2_ , ... )    |
 
 
 Using these patterns, a great diversity in surface forms that all map onto canonical uniform with one of the six
 special head symbols: List, ref, Tuple, call, Object, and Block.  
 
 Notice that, among many other language constructs, all of JSON just became a subset of Uniform.
 Further, based on the rules mapping Uniform onto JSON shown above, any JSON expression parsed into Uniform
 will map back to a JSON expression equal to the original.  (The many mapping guarantees of the Uniform 
 language are discussed in the Formal Guarantees section.)
 
 

<h4> Infix forms

Different modern programming languages include different operators with different meanings.  Still alot of the 
reason why the human viewers find these infix forms so easy to read, is because all of these languages seem
to follow common **_precedence_** rules for combining these operators.  So '*' binds tighter than '+', which is 
tighter than '==', then '&&', then '='

Uniform encodes these 'standard' prefix and infix operators, and maps those surface forms onto Uniform in the 
obvious way.  As an example here is the extended, canonical, and JSON forms for the same expression.  
All are parsable by Uniform, and all are EQUAL to each other.


|                    | **PREFIX / INFIX OPERATORS** |
| ------------------ | ---------------------------- |
| Format             | _expr_ **OP** _expr_         |
| Examples           | **--** decrement <br> x**2 + y**2| 
|  as uni-form       | "+"( "**"(x, 2), "**"(y, 2) )  |
|  as a JSON         | {"^":"+", "^1": {"^":"**", "^1":"x", "^2":2}, {"^":"**", "^1":"y", "^2":2} } |

<br><br>


 <h4> Statement Forms
 
 Uniform includes variational form which allow for traditional whitespace insensitive code forms similar to C, C++, 
 Java, Scala, Go, etc..  A second variational form allows for whitespace sensitive code forms that eliminate 
 braces, and use indention to encode structure.  Both forms have strong advantage for certain types of data,
 so Uniform doesn't make you choose!  Both surface forms parse down to equivalent Canonical Uniform or JSON.
 
 The C/C++/Java/Scala/Go-ish parsing is performed by the whitespace insensitive brace signaled by the leading
 ````{'''' character.  Statements in the form include traditioanl JSON forms, and previously seen Canonical Uniform,
 but this variational form extends parsing to allow uniform forms that do not have separating commas, or open / closing 
 parens.  
 
As a special cases:
  - Uniform allows block forms to stand in as the ending of a statement instead of a semi-colon
  - Uniform allows one to omit the trailing semi-colon at the end of a block. 
  - An unquoted token beginning with an alpha character is mapped to a _symbol_ expression, ````sym('token')````.
    This allows syntactic forms that use such token in their structure.
  - "#" and "//" both indicate the beginning of a comment that extends to the end of the current line.
    
 Putting these rules together we see each of these very natural looking statements that map in a resonable way 
 onto canonical uniform.
 
 ````
 # these Uniform statements look like C or Java
 while x>0 { 
     print "X is %s" % x; --x 
 }
 
 # yet they parse in the obvious way into an equivalent canonical Uniform expression:
 while( "<"(x(), 0), 
       Block( print( "%"("X is %s", x()) )
              "--"(x())
       )
 )

 
# Even surprisingly language-specific constructs are still expressible in Uniform:
{
    class MyClass extends (OtherClass, LastClass) {
    
        def nonsense_fn(int x, int y, z:5) {
            with open("/tmp/hello.txt", mode: "w+") as: f {
                f.write("hello world");
            }
        }
    }
}
 
 # This is the real power of Uniform.
 # It lets one easily invent ones own specialized language with ones own natural looking specialized constructs, 
 # all without worrying with syntax or parsers at all!  The underlying JSON is pretty much already in the parsed 
 # form that one would want to output from a specialized language parser.  No work required!
 ````
 
 
<h4> YAML forms
 
Even with all flexibility afforded by modern programming languages, there is still a place for YAML.
It allows the expression of static data-structures in a visually compelling form.  
YAML form allows embedding of arbitrary other syntax without complex and visually disastrous back-quoting, and 
uses whitespace sensitivity to enable unambiguous nesting over very large structures without any possibility of 
missing a closing brace, close quote, or having ones indention different than ones nesting.  These kinds of errors
are the primary reason why direct reading or editing of large JSON structures is hair pulling suicide inducing 
endeavor that humans should never be subjected to.

The full YAML language itself can be embedded into Uniform at any point as indicated by the '---' document initiator.
It either extends to the '...' document terminator, or to a line whose indention is LESS than the beginning of the
initiator.  Since YAML already maps to JSON and JSON maps to uniform, we know what the uniform expression for these
YAML inserts will be.  In the case that multiple YAML documents are inserted in a sequence, then that sequence is
wrapped in as List(...) uniform expression.

The fields of YAML are always strings, yet the value of Uniform is in its ability to parse those strings into recursive
Uniform expressions.  Thus we add the '::' operator.  Like a YAML document it can encode lists and maps into 
whitespace sensitive visual structure.  but the difference is that each of its fields are parsed according to the 
uniform language.  Within a colon-colon form the special (') operator is used to denote a string that does not require
back-quoting.

 


|                  | **WHITESPACE SENSITIVE BLOCK FORM**
| ---------------- | ---------------------------------------------------------------------------------- |
| Format           | **::** __head__ <br> &nbsp; &nbsp; &nbsp; &nbsp; ... <br> __key__ **::** __head__ <br>  &nbsp; &nbsp; &nbsp; &nbsp; ... |
| Examples         | ::Person <br> &nbsp; home :: Address 111 Maple lane  zip:=12345                    |
|   as uni-form:   |    Person( home=Address( "111 Maple lane", zip=12345 ) )                           |
|   as a JSON:     |    {"^":"Person", "home" : {"^":"Address", "^1":"111 Maple lane",  "zip":12345 } } |

The **::** form is the only whitespace sensitive form in the Uniform language.  This allows creation of deeply structured JSON objects without the nearly-impossible-to-diagnose errors from misaligned closing braces. (Modern editors detect mis-matched braces, but can provide no help if braces are balanced by do not convey the nesting expected by the user.)



<h4> Extensible Syntax



----------------------------------




|                   | **BLOCK FORM**                                           | 
| ----------------- | -------------------------------------------------------- |
| Format            | **{** stmt1 stmt2 ... **}**                              |
| Alternate form:   | { str = "looks like C code to me!"; print str }          |
|  as uni-form      | <code>block( "="(str, "looks like C code to me!"), <br> print(str))</code> |
|  as a JSON        | ```{"^":"block", "^1": {"^":"=", "^1":"str", "^2":"'looks like C code to me!"}, <br> {"^":"print", "^1":"str"} } ```|

Blocks are simply sequences of the statement forms as shown above.  Statements and blocks can be put together into complex structures that closely match common procedural idioms.  To show how natural and how flexible the block/statement parsing can be we provide this Uniform example followed by its uni-form equivelant:

```

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

This hat-trick allows Uniform to provide the best of all worlds: the best form for humans, the best form for machine, and a universal, purely-syntactic, bi-directional, lossless mapping which allows programmers to extend and invent new langauge constructs that continue to look good on the human side, continue to be trival to process on the machine side, and does not require them to mess with or alter the parsing/printing infrastructure at all!

The Uniform Langauge brings the advantages of homoiconicity to good old fashion procedural langauges w/o costing any of the readability typically associated with such languages.




<br><br>

## Other Uniform extensions


|                    | **COLON FORMS**              |
| ------------------ | ---------------------------- |
| Formats            | **{:** __key1__ **:=** __val1__ **,:**  ... **:}** <br> **[:** __val1__ **,:** ... **:]** <br> __head__ **(:**  __val1__ **,:** ... **,:** __key_a__ **:=** __val_a__ **,:**  ... **:)** <br> **'** some string |
| Examples           | {: key:='some value  then:=another(: 'value :) <br> &nbsp; &nbsp; a_list :== [: 'list ,: 'of values :] <br> some_function(: key:= val :)  :}  | 
|  as uni-form       | object( key: "some value", then: another("value"), a_list: ["list", "of values"] ) |

Uniform is designed to embed one source language into the fields of another.  These colon forms facilitate implicitly terminated strings (the **'** operator) which generally do not require escaping **"** or other syntax, since the colon forms themselves rarely occur within the source code of other languages.  (In those rare exceptional cases, a traditional backslash can still be used.)



COLON FORMS

SYMBOL FORM








# Appendix B

The careful reader might note some odd translations in the uni-form above, for example ' int(y) ' looks like we are passing y to some function called int.  Of course declaring a variable in any modern procedural language cannot be implemented by passing the variable to the "int-ifier" function.  But that is not the point here 

Certain forms (for example the if-elif-elif-else form requires some post processing, but as Appendix B shows, even that form fits into Uniform.  






##### STATEMENT FORM

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
used sexpr data structure.kl

At the bottom, all uniform source-code maps to a recursive application 
of the "UNI"-form itself.  The simplest presentation of the uni-form 
looks like a Python function call with keyword arguments.  The uni-form:

    head(VALUE1, VALUE2, ..., key_a=VALUE_A, key_b=VALUE_B, ...)     

The uni-form also maps trivially onto the JSON object notation:
   
     {'^':'head', '^1':VALUE1, '^2':VALUE2,  'key_a':VALUE_A, 'key_b:VALUE_B}

In uniform, values can either be a sub-uniform expression, or a JSON constant value like a string or number.  That's it.  That is the uni-form data structure.

##  xxxkl
kl



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

#Because Uniform is a slightly simplified verions of JSON, it is trivial to map between them.  
#Two special head values are used:  'object', and 'list'.  object( ... ) is the "uni"-form for a JSON 
#object that does not have any head ("^") key, and list( ... ) is the "uni"-form representation of a JSON list [ ... ].  




# end
---
Copyright (c)  Daniel Oblinger
