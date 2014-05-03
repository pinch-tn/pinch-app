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


// Is this needed?
$(document).ready(function() {
}
//  Select text highlighted
function setInputSelection(input, startPos, endPos) {
    input.focus();
    if (typeof input.selectionStart != "undefined") {
        input.selectionStart = startPos;
        input.selectionEnd = endPos;
    } else if (document.selection && document.selection.createRange) {
        // IE branch
        input.select();
        var range = document.selection.createRange();
        range.collapse(true);
        range.moveEnd("character", endPos);
        range.moveStart("character", startPos);
        range.select();
    }
    // return ???
}

//  Strikethrough selected text
function strikethroughSelected() {

	// Toggle strikethrough on highlighted text
	$("selected").toggle(
		function () {
	    	$(this).css({"list-style-type":"disc", "color":"blue"});
	  	},
	  	function () {
	    	$(this).css({"list-style-type":"disc", "color":"red"});
	  	},
	  	function () {
	    	$(this).css({"list-style-type":"", "color":""});
	  	}
	)
};
// Highlight selected and 
function highlightSelected() {
	// Toggle strikethrough on highlighted text
	$("selected").toggle(
		function () {
	    	$(this).css({"list-style-type":"disc", "color":"blue"});
	  	}
	    	$(this).css({"list-style-type":"", "color":""});
	  	}
	)
};

// Drag and Drop sticky notes
var adjustment
var item			// Needed?  For each sticky note

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



