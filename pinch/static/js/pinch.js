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

	var get_ticket_info = function(item) {
		var ticket_update = {
			workstream: item.parentNode.id,
			id: item.id,
			content: item.textContent,
			status: item.parentNode.parentNode.attributes["status"].nodeValue,
		};

	}


	// Add Sticky Note Button
	// Select the list that follows the button clicked
	var $current_list;
	$(".add").click(function() {
		$current_list = $(this).parent().next();
	});
	// Delete Sticky Note Button on each sticky note
	var deleteFunction = function ()
	{
		$(this).parent().remove();
		var pk = $(this).parent().attr("id")
		$.ajax("tickets/", {type: "delete", contentType: "application/json", data: JSON.stringify({pk: pk})})
	};
	// Take the text from the input from the modal
	$(".save").click(function() {
		var new_task_text = $(".modal-body input").val();  // "#myModal"
		var ticket_info = {
			workstream: $current_list.attr("id"),
			content: new_task_text,
			status: $current_list.parent().attr("status")
		};
		$.ajax("tickets/", {type:"post", contentType: "application/json", data: JSON.stringify(ticket_info), dataType:"json", success: function(data) {
			var $new_task = $("<li id='" + data.pk + "' class='ticket'><div class='trash'>x</div>" + new_task_text + "</li>");
			$current_list.append($new_task);
			$(".modal-body input").removeAttr('value');
			$(".trash").click(deleteFunction);
		}})
	});

	$(".trash").click(deleteFunction);

	// Drag and Drop sticky notes
	var adjustment



	$("ul.drag_list").sortable({
	  group: '.drag_list',
	  connectWith: '.drag_list',
	  pullPlaceholder: false,

		receive: function (event, ui) {
			var ticket_update = {
				workstream: ui.item[0].parentNode.id,
				pk: ui.item[0].id,
				content: ui.item[0].textContent.substring(1),
				status: ui.item[0].parentNode.parentNode.attributes["status"].nodeValue
			};
			console.log("Updating ticket status", ticket_update);
			$.ajax("tickets/", {type:"patch", contentType: "application/json", data: JSON.stringify(ticket_update)});
		},

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
