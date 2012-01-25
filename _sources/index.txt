hiddencode - A Sphinx Extension
===============================
Simple, inelegant Sphinx extension which adds a directive for a
highlighted code-block that may be toggled hidden and shown in HTML.  
Naturally, this directive is called ``hidden-code-block``.
This is possibly useful for teaching courses.

The directive, like the standard ``code-block`` directive, takes
a ``language`` argument and an optional ``linenos`` parameter.  The
``hidden-code-block`` adds ``starthidden`` and ``label`` as optional 
parameters.

Live Examples
-------------
Using ``starthidden`` to have the code initially showing:

.. hidden-code-block:: python
    :starthidden: False

    a = 10
    b = a + 5

Using ``label`` change the toggle text and ``linenos`` 
to include line numbers:

.. hidden-code-block:: python
    :linenos:
    :label: --- SHOW/HIDE ---

    x = 10
    y = x + 5

Installation
------------
Installing is as easy as downloading the 
`hidden_code_block.py <https://raw.github.com/scopatz/hiddencode/master/hidden_code_block.py>`_
file and placing it inside of your Sphinx project.  Then, edit the project's
``conf.py`` to include ``'hidden_code_block'`` in the extensions list
and add the current directory to the PYTHONPATH (``sys.path.insert(0, os.path.abspath('.'))``).

Acknowledgments
---------------
Thanks to http://www.javascriptkit.com/javatutors/dom3.shtml for   
inspiration on the javascript.      

Thanks to Milad 'animal' Fatenejad for suggesting this extension 
in the first place.

Written by Anthony 'el Scopz' Scopatz, January 2012.

Released under the WTFPL (http://sam.zoy.org/wtfpl/).

