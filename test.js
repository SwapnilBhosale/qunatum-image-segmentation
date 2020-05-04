const axios = require('axios');
const RFC_PATH = 'https://tools.ietf.org/rfc/rfc';
const MAX = 8000;


const encode = async input=>{
	return await Promise.all([...input].map(async letter=>{
		return await encodeLetter(letter);	
	}));
}

const encodeLetter = async letter => {
	let result = [];
	for(let i = 0; i < 10; i++){
		try {
			result[0] = ((Math.floor(Math.random() * MAX))+1);
			result[1] = (await axios.get(RFC_PATH + result[0]+ '.txt').catch(e=>console.error(e))).data.lastIndexOf(letter);
			if(result[1] === -1) continue;
			break;
		}catch(e){
			console.error(e);
		}
	}
	return result;
}
const init = async ()=>{
    arr = [ [ 3698, 17441 ], [ 5762, 37502 ], [ 4338, 75533 ], [ 582, 1511 ], [ 4672, 50778 ], [ 7649, 27677 ], [ 1703, 4077 ], [ 5455, 16771 ], [ 2498, 17377 ], [ 3970, 88787 ], [ 4960, 345925 ], [ 7983, 24856 ], [ 817, 45916 ], [ 4309, 28988 ], [ 5326, 120530 ], [ 7034, 27069 ], [ 2022, 189211 ], [ 6930, 23538 ], [ 2409, 51062 ] ];
    arr.forEach(function(val, i){encode(val).then(res => console.log(res));});
	
}
init();
