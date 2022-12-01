console.log("Hello, this is a test"); 

class Sonar_parser {
    constructor() {
        const input_data = this.load_input();
        let depths = [];
        input_data.forEach(line => {
            this.depths.add(line);                        
        });
    }
}

function get_depths(Sonar_parser parser) {
    return parser.depths;
}


