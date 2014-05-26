// Project specific Javascript goes here.

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
		self.selections.removeAll();
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
		console.debug("  Highlight class will be: ", highlightClass);

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
			console.debug("Adding selection", selectionArray(), selectionItem);
			selectionArray.push(selectionItem);
			console.debug("Selection array updated", selectionArray());
		});

	},
	update: function(element, valueAccessor, allBindings, viewModel, bindingContext) {
		console.debug("Updating highlight markings...");
		var currentSelections = valueAccessor().data();
		console.debug("Current selections are: ", currentSelections);
		var editor = element.editor;
		var highlightClass = valueAccessor().highlightClass;

		var $stricken = editor.getAllMarks();
		for (var j = 0; j < $stricken.length; j++) {
			$stricken[j].clear()
		}
		for (var i = 0; i < currentSelections.length; i++)
		{
			var currentSelection = currentSelections[i];
			console.debug("Highlighting section", currentSelection);
			editor.doc.markText({ line: currentSelection.line, ch: currentSelection.statement_start },
			                    { line: currentSelection.line, ch: currentSelection.statement_end },
			                    { className: highlightClass, atomic: false });
		}
	}
};


$(document).ready(function() {

});
