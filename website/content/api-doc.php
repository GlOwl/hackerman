<h2 class="my-4">Online API</h2>
<h3>Single Quotes</h3>
<p>Get a single random generated quote at:</p>
<p><code>hackerman.wtf/api</code></p>
<p>Returned is JSON file:</p>
<p><code>{ "quotes": ["Quantum LCDs restrict a UTF-8."] }</code></p>
<p><a href="/api" class="btn btn-primary mb-4" type="button" target="_blank">Try it out</a></p>

<h3>Multiple Quotes</h3>
<p>Get multiple random generated quotes at:</p>
<p><code>hackerman.wtf/api?n=3</code></p>
<p>
  The parameter 'n' sets the number of requested quotes (max. 100 per query).<br>
  Returned is a JSON file:
</p>
<p>
  <code>
    { "quotes": [
        "A system framework addresses a system.",
        "The common model will identify the key.",
        "A virus framework addresses a random framework."
      ] }
  </code>
</p>
<p><a href="/api?n=3" class="btn btn-primary mb-4" type="button" target="_blank">Try it out</a></p>

<h3>CSV Format</h3>
<p>Get quotes in CSV format at:</p>
<p><code>hackerman.wtf/api?n=3&f=csv</code></p>

<p>
  The parameter 'n' sets the number of requested quotes (max. 100 per query).<br>
  The parameter 'f' sets the format, allowed is 'csv' and 'json' (default = json).<br>
  Returned is a CSV file:
</p>
<p>
  <code>
    A bandwidth will address a spacetime algorithm.<br>
    Build the UTF-8 bandwidth, then you can build LCD models!
  </code>
</p>
<p><a href="/api?n=3&f=csv" class="btn btn-primary mb-4" type="button" target="_blank">Try it out</a></p>

<h3>Random Seed</h3>
<p>Get quotes generated using your own seed at:</p>
<p><code>hackerman.wtf/api?s=123</code></p>

<p>
  The parameter 's' sets the random seed string.<br>
  Returned is a JSON file:
</p>
<p>
  <code>{"quotes": ["Proprietary e-mails build a string."]}</code>
</p>
<p><a href="/api?s=123" class="btn btn-primary mb-4" type="button" target="_blank">Try it out</a></p>

<h2 class="my-4">Offline Python Script</h2>
<p>
  No internet, no problem! If you like to generate quotes on your own machine, you can!<br>
  Just visit our <a href="https://github.com/GlOwl/hackerman#local-generator-script" target="_blank">Github</a>
  and run the python script that is creating these quotes.
</p>
