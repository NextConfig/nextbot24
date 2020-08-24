//Cosas que ni a tu madre le importan :D/////////////////////////////////////////////////////////////////////
const Discord = require("discord.js");
const client = new Discord.Client();

client.login("NzQ2MDAzNTY1NzY3ODE5MzM1.Xz5_9g.XZyeuQVNGp848Y1fPiuSTZYsakE");

client.on('ready', () => {
   console.log('Estoy listo!');
   client.user.setActivity(`Estoy en ${client.guilds.cache.size} servidores | Usa /help`);
});

//CHATS DEL BOT AMISTOSOS :v////////////////////////////////////////////////////////////////////////////////////////
client.on('message', (message) => {
  if(message.content.startsWith('ping')) {
    message.channel.send('pong 🏓 (23+ MS / Api``22``)');
}});

client.on('message', (message) => {
  if(message.content.startsWith('Ping')) {
    message.channel.send('pong 🏓 (23 MS / Api``22``)');
}});

client.on('message', (message) => {
  if(message.content.startsWith('hola')) {
    message.channel.send(":v: ¡Hola!, ¿como estás? :heart:");
}});

client.on('message', (message) => {
  if(message.content.startsWith('Hola')) {
    message.channel.send(":v: ¡Hola!, ¿como estás? :heart:");
}});


//COMANDOS DEL BOT/////////////////////////////////////////////////////////////////////////////
client.on("message", message =>{

  let autor = message.author;
  
  if(message.content === "/help"){
  const embed = new Discord.MessageEmbed()
  .setTitle(":iphone: Ayuda de NextBot (Prueba) :iphone:")
  .setAuthor(autor.username, message.author.displayAvatarURL())
  message.channel.send({embed: {
    color: 3447003,
    title: ":iphone: **AYUDA DE**   :regional_indicator_n: :regional_indicator_e: :regional_indicator_x: :regional_indicator_t: :regional_indicator_b: :regional_indicator_o: :regional_indicator_t: ",
    description: "Obten ayuda sobre los comandos / chats",
    fields: [{
        name: "/help",
        value: "Muestra la lista de comandos / chats del bot"
      },
      {
        name: "/invite",
        value: "Obtén el link de invitacion del bot"
      },
      {
        name: "/yt",
        value: "Podrás ver el canal de youtube del creador"
      },
      {
        name: "/suicide",
        value: "Para tus días tristes :C"
      },
      {
        name: "/kill persona",
        value: "¡Mata a tu peor enemigo con estilo!"
      },
      {
        name: "/SOS",
        value: "Podrás mandar un mensaje de socorro al dueño del bot"
      },
      {
        name: "ping",
        value: "El bot te responderá"
      },
      {
        name: "hola",
        value: "El bot te respondera amistosamente"
      }
    ],
    timestamp: new Date(),
    footer: {
      author: {
        name: autor.displayAvatarURL,
        iconurl: client.user.avatarURL()
    },
  }
  }
})}})

client.on("message", message =>{

  let autor = message.author;
  
if(message.content === "/yt"){
  const embed = new Discord.MessageEmbed()
  .setTitle("xdd ")
  .setAuthor(autor.username, message.author.displayAvatarURL())
  message.channel.send({embed: {
    color: 3447003,
    title: ":regional_indicator_y: :regional_indicator_o: :regional_indicator_u: :regional_indicator_t: :regional_indicator_u: :regional_indicator_b: :regional_indicator_e:",
    description: "Por favor, suscribete a mi canal, no te arrepentiras!",
    fields: [{
      name: "Canal: ",
      value: "https://www.youtube.com/channel/UCrCeX8jN4PsjfozVQ-c6TQw?view_as=subscriber"
    },
    ],
    timestamp: new Date(),
    footer: {
      author: {
        name: autor.displayAvatarURL,
        iconurl: client.user.avatarURL()
    },
  }
  }
}
  )}});

let prefix = "/";

client.on("message", message =>{
const args = message.content.slice(prefix.lenght).trim().split(/ +/g);
const command = args.shift().toLowerCase();
if(command === '/sos'){
let texto = args.join("");
if(!texto) return message.channel.send(`Escriba el contenido a enviar.`);
message.channel.send(':white_check_mark: Su mensaje ha sido enviado al creador del bot');
client.users.cache.get('491285725384409088').send(texto)
}});

client.on("message", message =>{
  const args = message.content.slice(prefix.lenght).trim().split(/ +/g);
  const command = args.shift().toLowerCase();
  if(command === '/kill'){
  let texto2 = args.join("");
  if(!texto2) return message.channel.send(`Escriba a quien quieres matar.`);
  message.channel.send(`:white_check_mark: Su pedido de matar a ${args.join('texto2')} ha sido aceptado`)
  message.channel.send('https://tenor.com/view/kill-me-now-just-hell-gif-12524849')
}});

client.on('message', (message) => {
  if(message.content.startsWith('/suicide')) {
    message.channel.send("Muere rata asquerosaaaaaaaa, lajdñajdad");
    message.channel.send("https://tenor.com/view/kermit-shoot-lol-gun-frog-gif-16181496");
}});

client.on('message', (message) => {
    if(message.content.startsWith('/invite')) {
      message.channel.send(":v: ¡Hola!, este es mi link: **https://discord.com/oauth2/authorize?client_id=746003565767819335&permissions=8&scope=bot**");
  }});

  client.on("message", message =>{

    let autor = message.author;
    
  if(message.content === ".sudo raid"){
    const embed = new Discord.MessageEmbed()
    .setTitle("xdd ")
    .setAuthor(autor.username, message.author.displayAvatarURL())
    message.channel.send({embed: {
      color: 3447003,
      title: "Comnando de raid ha sido activado, ¡no uses mal este comando!",
      description: "Borrar canales, banear / expulsar miembros, etc",
      fields: [{
        name: "Quiere de verdad raidear el discord?",
        value: "Escriba SI para raidear, escriba no para cancelar"
      },
      ],
      timestamp: new Date(),
      footer: {
        author: {
          name: autor.displayAvatarURL,
          iconurl: client.user.avatarURL()
      },
    }
    }
  }
    )}});

