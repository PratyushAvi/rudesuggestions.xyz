<template>
	<div class="content">
		<h1 class="header">rudesuggestions.xyz (not yet)</h1>
		<div class="testing">
			<div class="input_box">
				<input class="input_field" v-model="textData" @input="update" placeholder="Enter some text">
			</div>
			<p class="suggestions"><span class="suggestions_title">Suggestions:</span> {{returnData}}</p>
		</div>
		<div class="code_link">
			<a class="link_text" href="#">Link to Code</a>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'SmortAgent',
		data: function() {
			return {
				returnData: [],
				textData: "",
				suggestions: "",
				noSuggestion: false,
				jsonData: Object,
			};
		},
		methods: {
			update: function () {
				self.data = "[]";
				if (this.textData === "" || this.textData === " ") {
					this.returnData = [];
					this.suggestions = "";
				}

                let arr = this.textData.split(" ");
                var index = 0;  

                for(var i = arr.length - 1; i >= 0; i--) {
                    if (arr[i] === ".") {
                        index = i;
                        break;
                    }
                }
				if (arr[arr.length-1] == " " || arr[arr.length-1] == "") {
					arr = arr.slice(0, arr.length-1);
				}

                let param = "";
                let data = [];

                for(var k = 5; k > 0; k--) {

                    let param = arr.slice(Math.max(index, arr.length-k), arr.length).join(' ');

                    if (param === " " || param === "") {
                        return;
                    }
                    if (param.toLowerCase() in this.jsonData) {
                        data = this.jsonData[param.toLowerCase()];
                        break;
                    }
                }

				this.returnData = data;
				this.suggestions = this.returnData.toString();
                console.log(param, data);
			},
		},
		mounted: function() {
			// const json = require('../config/trie.json');
            const json = require('../config/smoller_smort_trie.json');
			this.jsonData = JSON.parse(JSON.stringify(json));
		}
	}
</script>

<style scoped>
	.testing {
		position: absolute;
		display: block;
		width: 70%;
		top: 50%;
		left: 50%;
		-webkit-transform: translate(-50%, -50%);
		-moz-transform: translate(-50%, -50%);
		-o-transform: translate(-50%, -50%); 
		transform: translate(-50%, -50%);
		text-align: center;
	}

	.header {
		color:white;
		padding: 1rem;
		font-size: 2rem;
    }

	.suggestions {
		color: #d4d4d4;
		font-style: italic;
		font-weight: 200;
		font-size: 1.4rem;
	}

	.suggestions_title {
		color: #ffffff;
	}

	.input_box {
		position: relative;
		width: 100%;
		margin-top: 10pxs;
		padding: 15px 0 0;
	}

	.input_field {
		width: 70%;
		position: relative;
		border: 0;
		border-bottom: 2px solid #525252;
		outline: 0;
		font-size: 1.3rem;
		font-weight: 800;
		color: white;
		background: transparent;
		transition: border-color 0.7s;
	}

	.input_field:focus {
		border-bottom: 2px solid #2d70bd;
		transition: border-color 0.7s;
	}

	.code_link {
		position: absolute;
		bottom: 0%;
		padding: 2rem;
		left: 50%;
		-webkit-transform: translate(-50%, 0%);
		-moz-transform: translate(-50%, 0%);
		-o-transform: translate(-50%, 0%); 
		transform: translate(-50%, 0%);
	}

	.link_text {
		color: #525252;
		font-size: 1.2rem;
		transition-duration: 0.4s;
	}

	.link_text:hover {
		color: #d4d4d4;
		transition-duration: 0.4s;
	}

	@media (max-width: 1200px) and (min-width: 700px) {
		.suggestions {
			font-size: 1.3rem;
		}

		.input_field {
			font-size: 1.2rem;
			width: 80%;
		}

		.header {
			font-size: 1.5rem;
		}
	}

	@media (max-width: 700px) {
		.suggestions {
			font-size: 0.7rem;
		}

		.input_field {
			font-size: 0.8rem;
			width: 90%;
		}

		.header {
			font-size: 1.1rem;
		}


	}
</style>