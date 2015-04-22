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

function WorkstreamStatusModel(wsName, status, tickets)
{
	var self = this;
	self.wsName = wsName;
	self.status = status;
	self.tickets = ko.observableArray([]);

	for (var i = 0; i < tickets.length; i++)
	{
		self.tickets.push(new TicketModel(tickets[i]))
	}
	self.deleteTicket = function (ticket)
	{
		$.ajax("tickets/", { type: "delete", contentType: "application/json", data: JSON.stringify({id: ticket.id()}),
			success: function (data)
			{
				console.log("successfully deleted ticket", ticket);
				self.tickets.remove(ticket);
			},
			error: function (textStatus, errorThrown)
			{
				console.log("failed to delete ticket", textStatus, errorThrown);
			}
		});
	};
	self.updateToThis = function (arg)
	{
		console.log("updating ticket to " + self.status, arg.item)
		var ticket = arg.item;
		var ticket_update = {
			id: ticket.id(),
			content: ticket.text(),
			workstream: self.wsName(),
			status: self.status
		};

		$.ajax("tickets/", { type: "patch", contentType: "application/json", data: JSON.stringify(ticket_update),
			success: function (data)
			{
				console.log("successfully moved ticket to new status", ticket, self.status);
			},
			error: function (textStatus, errorThrown)
			{
				console.log("failed to move ticke to new status", textStatus, errorThrown);
			}
		});
	}
}

function WorkstreamModel(name, readyTickets, doingTickets, doneTickets)
{
	this.name = ko.observable(name);
	this.cssClass = ko.computed(function ()
	                            {
		                            return convertToSlug(this.name());
	                            }, this);
	this.ready = new WorkstreamStatusModel(this.name, "ready", readyTickets);
	this.doing = new WorkstreamStatusModel(this.name, "doing", doingTickets);
	this.done = new WorkstreamStatusModel(this.name, "done", doneTickets);

	var self = this;
	this.newText = ko.observable("");
	this.createNew = function ()
	{
		console.log("creating new ticket", self.newText());
		var ticket_info = {
			workstream: self.name(),
			content: self.newText(),
			status: "ready"
		};
		var pendingTicket = new TicketModel({id: -1, text: self.newText()});
		self.newText("");
		$.ajax("tickets/", { type: "post", contentType: "application/json", data: JSON.stringify(ticket_info), dataType: "json",
			success: function (data)
			{
				console.log("Created ticket on server", data);
				pendingTicket.id(data.id);
				self.ready.tickets.push(pendingTicket);
			},
			error: function (textStatus, errorThrown)
			{
				console.log("Error trying to create new ticket on server", textStatus, errorThrown);
			}
		});
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

$.ajax("tickets/", { dataType: "json", success: function (data)
{
	ko.applyBindings(new GravityBoardModel(data));
}, error: function (textStatus, errorThrown)
{
	console.log("Error trying to retrieve tickets from server", textStatus, errorThrown);
} });

$('.info-modal').modal('show');
