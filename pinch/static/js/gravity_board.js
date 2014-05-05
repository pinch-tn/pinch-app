ko.bindingHandlers.showModal = {
	init: function (element, valueAccessor)
	{
	},
	update: function (element, valueAccessor)
	{
		var value = valueAccessor();
		if (ko.utils.unwrapObservable(value))
		{
			$(element).modal('show');
			// this is to focus input field inside dialog
			$("input", element).focus();
		}
		else
		{
			$(element).modal('hide');
		}
	}
};

function convertToSlug(Text)
{
	return Text
		.toLowerCase()
		.replace(/[^\w ]+/g, '')
		.replace(/ +/g, '-')
		;
}

function TicketModel(ticket)
{
	this.id = ko.observable(ticket.id);
	this.text = ko.observable(ticket.text)

}

function WorkstreamStatusModel(status, tickets)
{
	this.status = status;
	this.tickets = ko.observableArray([]);

	for (var i = 0; i < tickets.length; i++)
	{
		this.tickets.push(new TicketModel(tickets[i]))
	}
	var self = this;
	this.deleteTicket = function (ticket)
	{
		$.ajax("tickets/", { type: "delete", contentType: "application/json", data: JSON.stringify({id: ticket.id()}), success: function (data)
		{
			console.log("successfully deleted ticket", ticket);
			self.tickets.remove(ticket);
		}, error: function (textStatus, errorThrown)
		{
			console.log("failed to delete ticket", textStatus, errorThrown);
		} });
	};
}

function WorkstreamModel(name, readyTickets, doingTickets, doneTickets)
{
	this.name = ko.observable(name);
	this.cssClass = ko.computed(function ()
	                            {
		                            return convertToSlug(this.name());
	                            }, this);
	this.ready = new WorkstreamStatusModel("ready", readyTickets);
	this.doing = new WorkstreamStatusModel("doing", doingTickets);
	this.done = new WorkstreamStatusModel("done", doneTickets);

	var self = this;
	this.newTicket = new TicketModel({id: -1, text: ""});
	this.createNew = function ()
	{
		console.log("creating new ticket", self.newTicket);
		ticket_info = {
			workstream: self.name(),
			content: self.newTicket.text(),
			status: "ready"
		};
		pendingTicket = self.newTicket;
		self.newTicket = new TicketModel({id: -1, text: ""});
		$.ajax("tickets/", { type: "post", contentType: "application/json", data: JSON.stringify(ticket_info), dataType: "json", success: function (data)
		{
			console.log("Created ticket on server", data);
			pendingTicket.id(data.id);
			self.ready.tickets.push(pendingTicket);
		}, error: function (textStatus, errorThrown)
		{
			console.log("Error trying to create new ticket on server", textStatus, errorThrown);
		}});
	};
}

function GravityBoardModel(workstreams)
{
	this.workstreams = ko.observableArray([]);
	for (var i = 0; i < workstreams.length; i++)
	{
		var ws = workstreams[i];
		this.workstreams.push(new WorkstreamModel(ws.name, ws.ready, ws.doing, ws.done));
	}
	this.currentWorkstream = ko.observable();
}

var mockTicketSetup = [
	{
		name: "first stream",
		ready: [
			{
				id: 1,
				text: "ticket 1"
			},
			{
				id: 2,
				text: "ticket 2"
			}

		],
		doing: [
			{
				id: 3,
				text: "ticket 3"
			},
			{
				id: 4,
				text: "ticket 4"
			}

		],
		done: [
			{
				id: 5,
				text: "ticket 5"
			},
			{
				id: 6,
				text: "ticket 6"
			}

		]
	},
	{
		name: "second stream",
		ready: [
			{
				id: 11,
				text: "ticket 11"
			},
			{
				id: 12,
				text: "ticket 12"
			}

		],
		doing: [
			{
				id: 13,
				text: "ticket 13"
			},
			{
				id: 14,
				text: "ticket 14"
			}

		],
		done: [
			{
				id: 15,
				text: "ticket 15"
			},
			{
				id: 16,
				text: "ticket 16"
			}

		]
	},
	{
		name: "third stream",
		ready: [
			{
				id: 21,
				text: "ticket 21"
			},
			{
				id: 22,
				text: "ticket 22"
			}

		],
		doing: [
			{
				id: 23,
				text: "ticket 23"
			},
			{
				id: 24,
				text: "ticket 24"
			}

		],
		done: [
			{
				id: 25,
				text: "ticket 25"
			},
			{
				id: 26,
				text: "ticket 26"
			}

		]
	},
	{
		name: "Tools and Technology",
		ready: [
			{
				id: 31,
				text: "ticket 31"
			},
			{
				id: 32,
				text: "ticket 32"
			}

		],
		doing: [
			{
				id: 33,
				text: "ticket 33"
			},
			{
				id: 34,
				text: "ticket 34"
			}

		],
		done: [
			{
				id: 35,
				text: "ticket 35"
			},
			{
				id: 36,
				text: "ticket 36"
			}

		]
	}
];

$.ajax("tickets/", { dataType: "json", success: function (data)
{
	ko.applyBindings(new GravityBoardModel(data));
}, error: function (textStatus, errorThrown)
{
	console.log("Error trying to retrieve tickets from server", textStatus, errorThrown);
} });
