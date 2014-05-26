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
			editor.doc.markText({line: currentSelection.line, ch: currentSelection.statement_start}, {line: currentSelection.line, ch: currentSelection.statement_end}, options)
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
					var lineNo = line.lineNo()
					for (var k = 0; k < line.markedSpans.length; k++) {
						var markedSpan = line.markedSpans[k];
						selections.push({ "line":  lineNo, "statement_start": markedSpan.from, "statement_end": markedSpan.to });
						console.log("Span", markedSpan)
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

// bind an entire div to this model with "with"
//   bind a button to "clear"
//   bind a hidden input field to "selectionsJson"
//   bind a textarea to "selections" with "highlight" binding
//   the highlighted sections and the json in hidden input field will be kept in sync
//     we achieve this by updating the codemirror selections whenever the "selections" observable changes
//     we also update the "selections" observable whenever a new selection is made
//
function HighlightModel() {
	var self = this;

	self.clear = function() {
		self.selections.clear();
	};

	self.selections = ko.observableArray([]);

	self.selectionsJson = ko.computed(function() {
		return JSON.stringify(self.selections());
	});
}

// Bind to a text area, specify a "highlighted class"
ko.bindingHandlers.highlight = {
	init: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
		console.log("Setting up highlighting", element, allBindings);
		var highlightClass = valueAccessor().highlightClass;
		console.log("  Highlight class will be: ", highlightClass);

		var editor = CodeMirror.fromTextArea(element, {
			lineWrapping: true,
			readOnly: true
		});
		element.editor = editor;
		// Make the manipulation occur on the mouseup interaction
		var lastSel = undefined;
		editor.on('cursorActivity', function() {
			lastSel = editor.doc.listSelections()[0];
		});
		var el = editor.getWrapperElement();
		$(el).mouseup(function() {
			var sel = lastSel;
			console.log("Recording selection", sel);
			var selectionArray = valueAccessor().data;
			var selectionItem;
			if (sel.head.ch > sel.anchor.ch) {
				selectionItem = { line: sel.head.line, statement_start: sel.anchor.ch, statement_end: sel.head.ch};
			} else {
				selectionItem = { line: sel.head.line, statement_start: sel.head.ch, statement_end: sel.anchor.ch};
			}
			console.log("Adding selection", selectionArray(), selectionItem);
			selectionArray.push(selectionItem);
			console.log("Selection array updated", selectionArray());
		});

	},
	update: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
		console.log("Updating highlight markings...");
		var currentSelections = valueAccessor().data();
		console.log("Current selections are: ", currentSelections);
		var editor = element.editor;
		var highlightClass = valueAccessor().highlightClass;
		for (var i = 0; i < currentSelections.length; i++)
		{
			var currentSelection = currentSelections[i];
			console.log("Highlighting section", currentSelection);
			editor.doc.markText({ line: currentSelection.line, ch: currentSelection.statement_start },
			                    { line: currentSelection.line, ch: currentSelection.statement_end },
			                    { className: highlightClass, atomic: false });
		}
	}
};


$(document).ready(function() {

//	setup_highlighting("#strike_statement", "#minify_next", "redactions", function() {
//		return {
//			className: 'strikethrough',
//			atomic: false
//		}
//	});

	setup_highlighting("#highlight_statement", "#highlight_next", "workstreams", function() {
		return {
			className: 'highlight',
			atomic: false
		}
	});

});
