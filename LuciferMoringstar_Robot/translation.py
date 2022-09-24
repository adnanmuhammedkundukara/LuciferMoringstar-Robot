# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot
# License Link : https://github.com/PR0FESS0R-99/LuciferMoringstar-Robot/blob/LuciferMoringstar-Robot/LICENSE

START_MESSAGE = """
👋Hello {mention}..!
​This bot can help you find and **share Telegram files.
It works in any chat, just write @ebooksdlsbot in the text field. Let's try!
ടെലിഗ്രാം ഫയലുകൾ കണ്ടെത്താനും പങ്കിടാനും ഈ ബോട്ട് നിങ്ങളെ സഹായിക്കും. 
ഇത് ഏത് ചാറ്റിലും പ്രവർത്തിക്കുന്നു, ടെക്സ്റ്റ് ഫീൽഡിൽ @ebooksdlsbot എന്ന് എഴുതുക. നമുക്ക് ശ്രമിക്കാം!**"""

HELP_MESSAGE = """
𝙷𝙴𝙻𝙻𝙾 {mention}
𝙸 𝙲𝙰𝙽 𝙶𝚄𝙸𝙳𝙴 𝚈𝙾𝚄 𝚃𝙷𝚁𝙾𝚄𝙶𝙷 𝙰𝙻𝙻 𝙾𝙵𝙵 [{name}](https://t.me/{username})', 𝙲𝙾𝙾𝙻 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙰𝙽𝙳 𝙷𝙾𝚆 𝚃𝙾 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝚄𝚂𝙴 𝚃𝙷𝙴𝙼. 𝚃𝙷𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙱𝙴𝙻𝙾𝚆 𝚃𝙾 𝙽𝙰𝚅𝙸𝙶𝙰𝚃𝙴 𝚃𝙷𝙴𝙾𝚄𝙶𝙷 𝙰𝙻𝙻 𝙾𝙵 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴𝚂
"""

ABOUT_MESSAGE = """
𝙱𝙾𝚃 𝚃𝚈𝙿𝙴 : EBOOKS
𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : [MUHAMMED ADNAN K](t.me/mr_readers)
𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : [{name}](https://t.me/{username})
𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽3 : {py3_version}
𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 : {pyro_version}
𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : {version}
𝚂𝙾𝚄𝚁𝙲𝙴 : [𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴]({source})
"""

SETTINGS_MESSAGE = """
**𝙲𝙷𝙰𝙽𝙶𝙴 𝚈𝙾𝚄𝚁 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂 𝙵𝙾𝚁 Change {title} 𝙰𝚂 𝚈𝙾𝚄𝚁 𝚆𝙸𝚂𝙷.⚙"""

CHAT_LOGS_MESSAGE = """
• **{title}**\n• `{id}`\n• **{join}**"""

SPELLMODE_MESSAGE = """
**__Hello 👋 {mention}**__
**__Couldn't Find {query} ?  Please Click Your Request Name**__"""

REQUEST_MESSAGE = """
**Requested By:** {mention}\n**Requested BOOK Name:** {query}\n™ {group_name}"""

WELCOME_MESSAGE = """
𝙷𝙴𝙻𝙻𝙾 {mention} 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 {group_name}"""

FILECAPTION_MESSAGE = """
• `{file_name}` \n 𝙹𝙾𝙸𝙽 : @EBOOKS_MALAYALAM_EBOOKS"""

ADMIN_CMD_MESSAGE = """
𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 :-
\n • /broadcast : 𝚁𝙴𝙿𝙻𝚈 𝙰𝙽𝚃 𝙼𝙴𝙳𝙸𝙰/𝙼𝚂𝙶\n • /total : 𝙶𝙴𝚃 𝙵𝙸𝙻𝙴𝚂 𝙲𝙾𝚄𝙽𝚃\n • /delete : 𝙳𝙴𝙻𝙴𝚃𝙴 𝚂𝙸𝙽𝙶𝙻𝙴 𝙵𝙸𝙻𝙴𝚂\n • /delall : 𝙳𝙴𝙻𝙴𝚃𝙴 𝙰𝙻𝙻 𝙵𝙸𝙻𝙴𝚂\n • /logs : 𝙶𝙴𝚃 𝙱𝙾𝚃 𝙻𝙾𝙶𝚂"""

STATUS_MESSAGE = """
× {bot_name} 𝚂𝚃𝙰𝚃𝚄𝚂 :-
× 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂 : {users}\n× 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂 : {files}\n× 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂 : {chats}"""

GETFILE_TEXT = """
𝙷𝙴𝚈 {mention} 𝚈𝙾𝚄𝚁 𝙵𝙸𝙻𝙴 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈
\n𝙵𝙸𝙻𝙴𝙽𝙰𝙼𝙴 : `{file_name}`\n\n𝙵𝙸𝙻𝙴𝚂𝙸𝚉𝙴 : {file_size}"""

NOT_SUB = """
𝙸 𝙻𝙸𝙺𝙴 𝚈𝙾𝚄𝚁 𝚂𝙼𝙰𝚁𝚃𝙽𝙴𝚂𝚂, 𝙱𝚄𝚃 𝙳𝙾𝙽'𝚃 𝙱𝙴 𝙾𝚅𝙴𝚁𝚂𝙼𝙰𝚁𝚃 😤.\n 𝙵𝚒𝚛𝚜𝚝 𝚂𝚞𝚋𝚜𝚌𝚛𝚒𝚋𝚎 𝙼𝚢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 😕"""              

× 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳 𝙱𝚈
  - [{}](t.me/{})"""



