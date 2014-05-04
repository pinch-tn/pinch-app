/* Project specific Javascript goes here. */


//	NO LONGER USING: Add feature for MVP statement 
// $(".add_feature").click(function(){
// 	// Add text field with Remove button when Add button clicked
// 	$("form").append("<div class='feature'><input name='feature' type='text'> <button id='remove'>Remove</button></div>")
// )};
// // Remove text field and Remove button when Remove button clicked
// $("#remove").click(function(){
// 	$(this).parent().remove();  
// });

// .CodeMirror-selected {background:#CCCCCC;}

$(document).ready(function() {
	var editor = CodeMirror.fromTextArea($('#strike_statement')[0], {
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
});


// doc.getAllMarks() → array<TextMarker>
// remove
// turn span's into variables

// var clear = editor.doc.getAllMarks().remove();  
// loop over array and call .remove() on each element



//     $("#strike_statement").click(function(){
// 		//  Select text highlighted
//         var highlight = window.getSelection(),  
//         spn = '<span class="highlight">' + highlight + '</span>',

//         text = $('#strike_statement').text(),						// strike_statement or other class? 
//         range = highlight.getRangeAt(0),
//         startText = text.substring(0, range.startOffset), 
//         endText = text.substring(range.endOffset, text.length);

// 		$('#strike_statement').html(startText + spn + endText);
// 	});
// });


// function getSelectionText() {
//     var text = "";
//     if (window.getSelection) {
//         text = window.getSelection().toString();
//     } else if (document.selection && document.selection.type != "Control") {
//         text = document.selection.createRange().text;
//     }
//     return text;
// }

//OR
// function setInputSelection(input, startPos, endPos) {
//     input.focus();
//     if (typeof input.selectionStart != "undefined") {
//         input.selectionStart = startPos;
//         input.selectionEnd = endPos;
//     } else if (document.selection && document.selection.createRange) {
//         // IE branch
//         input.select();
//         var range = document.selection.createRange();
//         range.collapse(true);
//         range.moveEnd("character", endPos);
//         range.moveStart("character", startPos);
//         range.select();
//     }
// }

//  Strikethrough selected text and remove
// function strikethroughSelected() {
// 	var $selected = getSelectionText(); 
// 	// Toggle strikethrough on highlighted text
// 	$selected.html("<span class='struck'></span>");
// }



// Drag and Drop sticky notes
// var adjustment
// var item			// Needed???  For each sticky note

// 	$(".workstream-column").sortable({
// 	  group: 'column',
// 	  pullPlaceholder: false,
// 	  // animation on drop
// 	  onDrop: function  (item, targetContainer, _super) {
// 	    var clonedItem = $('<li/>').css({height: 0})
// 	    item.before(clonedItem)
// 	    clonedItem.animate({'height': item.height()})
	    
// 	    item.animate(clonedItem.position(), function  () {
// 	      clonedItem.detach()
// 	      _super(item)
// 	    })
// 	  },

// 	  // set item relative to cursor position
// 	  onDragStart: function ($item, container, _super) {
// 	    var offset = $item.offset(),
// 	    pointer = container.rootGroup.pointer

// 	    adjustment = {
// 	      left: pointer.left - offset.left,
// 	      top: pointer.top - offset.top
// 	    }

// 	    _super($item, container)
// 	  },
// 	  onDrag: function ($item, position) {
// 	    $item.css({
// 	      left: position.left - adjustment.left,
// 	      top: position.top - adjustment.top
// 	    })
// 	  }
// 	});

