const data = {
    nodes: [
      {
        id: "Andrew Puglisi",
        total_abuse_count: 9,
        rank_incident: "Sergeant",
        precinct: 1
      },
      {
        id: "Brian Ilund",
        rank_incident: "Detective",
        total_abuse_count: 6,
        precinct: 1
      },
      {
        id: "Daniel Guerra",
        rank_incident: "Police Officer",
        total_abuse_count: 18,
        precinct: 1
      },
      {
        id: "Daniel Lee",
        rank_incident: "Police Officer",
        total_abuse_count: 50,
        precinct: 1
      },
      {
        id: "Andrew Wunsch",
        rank_incident: "Detective",
        total_abuse_count: 15,
        precinct: 1
      },

    ],
    links: [
      {
        source:
          "Brian Ilund",
        target: "Andrew Wunsch",
        value: 2,
      },
      {
        source:
          "Daniel Lee",
        target: "Andrew Puglisi",
        value: 15,
      },
      {
        source:
          "Daniel Guerra",
        target: "Andrew Wunsch",
        value: 50,
      },
    ],
  };


export default data;
