<blockquote class="blockquote mt-4 p-4 mb-0">
  <p class="text-success" id="quote"><?php echo $quote; ?></p>
  <button type="button" class="btn btn-info float-right" id="copy">Copy</button>
  <footer class="blockquote-footer">The Hackerman Quote Generator</footer>
</blockquote>

<div class="row">
  <div class="col-sm-6">
    <button type="button" class="btn btn-success btn-md btn-block mt-4" id="good-button">Nice one :D</button>
  </div>

  <div class="col-sm-6">
    <button type="button" class="btn btn-danger btn-block mt-4" id="bad-button">Meh :/</button>
  </div>

</div>

<div class="row">
  <div class="col-sm-6">
    <h3 class="py-4">The good stuff</h3>
    <div class="list-group" id="good-list"></div>
    <button type="button" class="btn btn-primary mt-4" id="download">Download</button>
  </div>

  <div class="col-sm-6">
    <h3 class="py-4">Left overs</h3>
    <div class="list-group" id="bad-list"></div>
  </div>
</div>
