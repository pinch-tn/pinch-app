// Project specific Javascript goes here. 


/********		 MINIFY MVP PAGE		********/
// Strikethrough text highlighted in minify phase
$(document).ready(function() {
	// Go to CodeMirror library for rendering & manipulating the text
	var editor = CodeMirror.fromTextArea($('#strike_statement')[0], {
		lineWrapping: true,
		readOnly: true
	});
	// Make the manipulation occur on the mouseup interaction
	var dblDebounceFn = function() {
		var sel = editor.doc.listSelections()[0];
		if (mouseDown) 
			return setTimeout(dblDebounceFn, 100);
		var options = {
			className: 'strikethrough',
			atomic: false
		};
		if (sel.head.ch > sel.anchor.ch) {
			editor.doc.markText(sel.anchor, sel.head, options);	
		} else {
			editor.doc.markText(sel.head, sel.anchor, options);
		}
	};
	var debounceFn = _.debounce(dblDebounceFn, 450);
	editor.on('cursorActivity', debounceFn);
	var mouseDown = false;
	var el = editor.getWrapperElement();
	$(el).mousedown(function() {
		mouseDown = true;
	}).mouseup(function() {
		mouseDown = false;
	});


	// Delete all struckthrough text
	$("#minify_next").click() = function() {
		$stricken = doc.getAllMarks();
		for (var item in $stricken) {
			item.remove();
		};
		// Read the next of the text into a variable for the next step
		minified_statement = $( "#strike_statement" ).text();
	};




/******** 		BREAKDOWN MVP PAGE 		********/
	var editor = CodeMirror.fromTextArea($('#highlight_statement')[0], {
		lineWrapping: true,
		readOnly: true
	});
	var dblDebounceFn = function() {
		var sel = editor.doc.listSelections()[0];
		if (mouseDown) 
			return setTimeout(dblDebounceFn, 100);
		var options = {
			className: 'highlight',
			atomic: false
		};
		if (sel.head.ch > sel.anchor.ch) {
			editor.doc.markText(sel.anchor, sel.head, options);	
		} else {
			editor.doc.markText(sel.head, sel.anchor, options);
		}
	};
	var debounceFn = _.debounce(dblDebounceFn, 450);
	editor.on('cursorActivity', debounceFn);
	var mouseDown = false;
	var el = editor.getWrapperElement();
	$(el).mousedown(function() {
		mouseDown = true;
	}).mouseup(function() {
		mouseDown = false;
	});


	// Take all highlighted spans and convert to workstream titles
	$("#breakdown_next").click() = function() {
		$highlighted = doc.getAllMarks();
		for (var item in $highlighted) {
			item.remove();
		};
		// Read the next of the text into a variable for the next step
		minified_statement = $( "#highlight_statement").text();
	};
});



// remove
// turn span's into variables

// var clear = editor.doc.getAllMarks().remove();  
// loop over array and call .remove() on each element











// Drag and Drop sticky notes
var adjustment
var item			// Needed???  For each sticky note

	$(".workstream-column").sortable({
	  group: 'column',
	  pullPlaceholder: false,
	  // animation on drop
	  onDrop: function  (item, targetContainer, _super) {
	    var clonedItem = $('<li/>').css({height: 0})
	    item.before(clonedItem)
	    clonedItem.animate({'height': item.height()})
	    
	    item.animate(clonedItem.position(), function  () {
	      clonedItem.detach()
	      _super(item)
	    })
	  },

	  // set item relative to cursor position
	  onDragStart: function ($item, container, _super) {
	    var offset = $item.offset(),
	    pointer = container.rootGroup.pointer

	    adjustment = {
	      left: pointer.left - offset.left,
	      top: pointer.top - offset.top
	    }

	    _super($item, container)
	  },
	  onDrag: function ($item, position) {
	    $item.css({
	      left: position.left - adjustment.left,
	      top: position.top - adjustment.top
	    })
	  }
	});

