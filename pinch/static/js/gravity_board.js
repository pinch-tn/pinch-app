function GravityBoardModel() {
	this.workstreams = ko.observableArray([
		                                      {
			                                      name: ko.observable("first stream"),
			                                      ready: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 1,
						                                                                  text: "ticket 1"
					                                                                  },
					                                                                  {
						                                                                  id: 2,
						                                                                  text: "ticket 2"
					                                                                  }

				                                                                  ])
			                                      },
			                                      doing: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 3,
						                                                                  text: "ticket 3"
					                                                                  },
					                                                                  {
						                                                                  id: 4,
						                                                                  text: "ticket 4"
					                                                                  }

				                                                                  ])
			                                      },
			                                      done: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 5,
						                                                                  text: "ticket 5"
					                                                                  },
					                                                                  {
						                                                                  id: 6,
						                                                                  text: "ticket 6"
					                                                                  }

				                                                                  ])
			                                      }
		                                      },
		                                      {
			                                      name: ko.observable("second stream"),
			                                      ready: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 11,
						                                                                  text: "ticket 11"
					                                                                  },
					                                                                  {
						                                                                  id: 12,
						                                                                  text: "ticket 12"
					                                                                  }

				                                                                  ])
			                                      },
			                                      doing: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 13,
						                                                                  text: "ticket 13"
					                                                                  },
					                                                                  {
						                                                                  id: 14,
						                                                                  text: "ticket 14"
					                                                                  }

				                                                                  ])
			                                      },
			                                      done: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 15,
						                                                                  text: "ticket 15"
					                                                                  },
					                                                                  {
						                                                                  id: 16,
						                                                                  text: "ticket 16"
					                                                                  }

				                                                                  ])
			                                      }
		                                      },
		                                      {
			                                      name: ko.observable("third stream"),
			                                      ready: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 21,
						                                                                  text: "ticket 21"
					                                                                  },
					                                                                  {
						                                                                  id: 22,
						                                                                  text: "ticket 22"
					                                                                  }

				                                                                  ])
			                                      },
			                                      doing: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 23,
						                                                                  text: "ticket 23"
					                                                                  },
					                                                                  {
						                                                                  id: 24,
						                                                                  text: "ticket 24"
					                                                                  }

				                                                                  ])
			                                      },
			                                      done: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 25,
						                                                                  text: "ticket 25"
					                                                                  },
					                                                                  {
						                                                                  id: 26,
						                                                                  text: "ticket 26"
					                                                                  }

				                                                                  ])
			                                      }
		                                      },
		                                      {
			                                      name: ko.observable("Tools and Technology"),
			                                      ready: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 31,
						                                                                  text: "ticket 31"
					                                                                  },
					                                                                  {
						                                                                  id: 32,
						                                                                  text: "ticket 32"
					                                                                  }

				                                                                  ])
			                                      },
			                                      doing: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 33,
						                                                                  text: "ticket 33"
					                                                                  },
					                                                                  {
						                                                                  id: 34,
						                                                                  text: "ticket 34"
					                                                                  }

				                                                                  ])
			                                      },
			                                      done: {
				                                      tickets: ko.observableArray([
					                                                                  {
						                                                                  id: 35,
						                                                                  text: "ticket 35"
					                                                                  },
					                                                                  {
						                                                                  id: 36,
						                                                                  text: "ticket 36"
					                                                                  }

				                                                                  ])
			                                      }
		                                      }
	                                      ])
}

ko.applyBindings(new GravityBoardModel());
