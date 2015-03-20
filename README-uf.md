

<h4>
UNIFORM provides for SOURCE-CODE what <br>
what YAML provides for LISTS:
</h4>



### a human enjoyable "obvious" markdown syntax which maps to the "obvious" underlying data structure.

Like YAML, UNIFORM is also:

* LOSSLESS -- Any source structure can be printed into a form, which parse back into a structure EQUAL to the original.

* PURELY SYNTACTIC -- Uniform parses a Java/Python/Scala/C-ish language in a generic, purely-syntactic way into 
  its underlying data structure.
  
* MARKDOWN-ish -- Like both markdown and YAML, Uniform has constructs optimized to look simple and beautiful in
  their UNICODE source format.
  
* OBVIOUS -- Like YAML, Uniform is designed to be "obvious".  Without reading any documentation, a software engineer
  should be able to view 'uniform' source and know what it means.  Without reading any documentation, they should
  also be able to know what recursive list and map structure any uniform code parses into.
  
* REDUNDANT -- Like YAML, multiple alternate forms are provided for the common underlying data-structure so
  the author can select a source format which allows any arbitrary data structure to be encoded in a way that
  is visually pleasing in the source format.  (e.g. YAML and Uniform provide compact one line formats plus multiline
  formats, so different ideal forms can be selected as needed.

* SINGULAR -- 

# The UNI-FORM syntax

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




## UNIFORM SYNTAX

The surface form of uni-form is a bit like YAML in that it provides
alternate representations for the same underlying uniform data in
order to improve human readability in specific cases.  Just as YAML
provides multiple representations for lists and maps, uniform provides
multiple representations for source-code like structures of if-s,
while-s, and function calls.  Below is a sample showing how complex
uniform source code, can still be quite human-readable.  And remember,
all of these source forms tri valley map to a uni-form expression, which
is encoded as a tree of JSON objects.  These forms are also easy to read
and manipulate programmatically too.



    -:- A motivating example showing alternate forms of the uniform language.
    ::Person
        name := 'Dan Oblinger
		funky_string := 'like YAML, string do not need back quoting.  even 
		                 multi-line strings with "quotes" and 'quotes' and back quotes \ are just fine.
        home :: Address '3403 Cesar Chavez   Apt := C  
                         City := San Francisco   State := CA   zip := 94110
        email := 'dan@oblinger.us
        friends := 'Qingling Ni ,: 'Jack Porter ,: 'Josh Yelon ,:
            ::Person  name:='Inline-defined Person                    -:- Notice this fourth friend is actually an in-line defined object
                      home::Address 1234 inline street address 
    		                City:=Some City  State:=CA  Zip:=12345
    
        theorems::
            a^2+b^2 == c^2                 -:- This is not a string, it is a recursive uniform code expression
    
        good_old_JSON_still_works_here::
            {'equation': ['equals', 'e', ['times' 'm' ['squared' 'c']]]}
    
        some_uniform_code::
            def factorial(x) {
    	        if x<=1 { 
    	            return 1; 
    	        } else { 
    	            return x * factorial(x-1);
    	        };                                  -:- Notice, the statement form requires ending semi-colons
            };
    
        some_embedded_source_code:: java         -:- Notice here we are embedding the source code of another language 
                                                 -:- and we are NOT added a bunch of '\' characters.
                                                 -:- try doing that in JSON, or really any other language!
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
these alternative forms simply aid in human-readability, but the
resulting data structure is always the same underlying uni-form expression.  


To get the jist of what you have seen above, here are examples of an
alternate form, a uni-form, and a JSON form.  All of three expressions
will parse into the SAME underlying JSON data:

    Alternate form:        x^2+y^2       
    as uni-form:           plus( power(x, 2), power(y, 2) )
	as a JSON form:        {'^':'plus', '^1': {'^':'power', '^1':'x', '^2':2}, {'^':'power', '^1':'y', '^2':2} }
.


    Alternate form:       ::Person
                              home :: Address 111 Maple lane  zip:=12345 
							  
    as uni-form:          Person( home=Address( "111 Maple lane", zip=12345 ) )
	
    as a JSON form:       {"^":"Person", "home" : {"^":"Address", "^1":"111 Maple lane",  "zip":12345 } }
.


	Alternate form:       if x==y then:
	                          return "Same"
    	                  else:
						      return "Different"
    	                  end

    as uni-form:          if( equal(x, y), then=return("Same"), else=return("Different"))
	
	as a JSON form:       {'^':'if', '^1': {'^':'equals', '^1':'x', '^2':'y'},
                               'then': {'^':'return', '^1':'Same'},
						       'else': {'^':'return', '^1':'Different'} }
.

    Alternate form:       java_source := 'system.out.println("embedded \"quotes\" and backquotes (\\) are a needless pain!");
	as a JSON form:       { "java_source": "system.out.println(\"embedded \\\"quotes\\\" and backquotes (\\\\) are a needless pain!\");", 


---
Copyright (c)  Daniel Oblinger
