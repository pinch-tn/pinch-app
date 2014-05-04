// Project specific Javascript goes here. 

function setup_highlighting(text_selector, button_selector, field_name, options_callback)
{
	var target = $(text_selector)[0];
	if (target) {
		console.log("Setting up highlighting for " + text_selector);
		var editor = CodeMirror.fromTextArea(target, {
			lineWrapping: true,
			readOnly: true
		});
		// Make the manipulation occur on the mouseup interaction
		var lastSel = undefined;
		var dblDebounceFn = function() {
			lastSel = editor.doc.listSelections()[0];
		};
//	var debounceFn = _.debounce(dblDebounceFn, 450);
		editor.on('cursorActivity', dblDebounceFn);
		var el = editor.getWrapperElement();
		$(el).mouseup(function() {
			console.log("marking selection", lastSel.head.ch, lastSel.anchor.ch);
			var options = options_callback();
			var sel = lastSel;
			console.log("Recording selection", sel)
			if (sel.head.ch > sel.anchor.ch) {
				editor.doc.markText(sel.anchor, sel.head, options);
			} else {
				editor.doc.markText(sel.head, sel.anchor, options);
			}
		});

		var currentSelections = JSON.parse($("#selections").val());
		for (var i = 0; i < currentSelections.length; i++)
		{
			var currentSelection = currentSelections[i];
			var options = options_callback();
			editor.doc.markText({line: 0, ch: currentSelection.statement_start}, {line:0, ch: currentSelection.statement_end}, options)
		}

		// Delete all struckthrough text
		$(button_selector).click( function() {
			console.log("hi");
			var $stricken = editor.getAllMarks();
			console.log($stricken);
			var selections = [];
			for (var i = 0; i < $stricken.length; i++) {
				var textMarker = $stricken[i];
				for (var j = 0; j < textMarker.lines.length; j++) {
					var line = textMarker.lines[j];
					for (var k = 0; k < line.markedSpans.length; k++) {
						var markedSpan = line.markedSpans[k];
						selections.push({ "statement_start": markedSpan.from, "statement_end": markedSpan.to });
						console.log("Span", markedSpan.from, markedSpan.to)
					}
				}
			}
			$("#selections").val(JSON.stringify(selections));
		});

		$("#clear").click( function() {
			console.log("Clearing all selections...")
			var $stricken = editor.getAllMarks();
			for (var i = 0; i < $stricken.length; i++) {
				$stricken[i].clear()
			}
		})
	}
}
$(document).ready(function() {

	setup_highlighting("#strike_statement", "#minify_next", "redactions", function() {
		return {
			className: 'strikethrough',
			atomic: false
		}
	});

	setup_highlighting("#highlight_statement", "#highlight_next", "workstreams", function() {
		return {
			className: 'highlight',
			atomic: false
		}
	});


// loop over array and call .remove() on each element
// var $ticket = $('<div class="task-header"><textarea></textarea></div>');
// $button_name.click(function() {

// });








	// Drag and Drop sticky notes
	var adjustment
	var item			// Needed???  For each sticky note

	$(".task-columns").sortable({
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
});
