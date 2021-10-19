<template>
	<div class="content">
		<h1 class="header">rudesuggestions.xyz</h1>
		<div class="testing">
			<div class="input_box">
				<input class="input_field" v-model="textData" @input="update" placeholder="Enter some text">
			</div>
			<p class="suggestions"><span class="suggestions_title">Suggestions:</span> {{returnData}}</p>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Main',
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
				let ignoreList = [',', ';'];
				if (this.textData === "" || this.textData === " " || this.textData[this.textData.length - 1] in ignoreList) {
					this.returnData = [];
					this.suggestions = "";
				}
				let arr = this.textData.split(" ");
				let param = arr[arr.length - 1];
				if (param === " " || param === "") {
					return;
				}
				let data = [];
				if (param.toLowerCase() in this.jsonData) {
					data = this.jsonData[param.toLowerCase()];
				}
				this.returnData = data;
				this.suggestions = this.returnData.toString();
				console.log(param, this.suggestions);
			},
		},
		mounted: function() {
			const json = require('../config/trie.json');
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