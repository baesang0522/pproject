from pproject.keyword_extraction.rake_nltk import rake_keyword_extract
from pproject.keyword_extraction.spacy import spacy_keyword_extract
from pproject.keyword_extraction.yake import yake_keyword_extract
from pproject.db_connect.wco_query import article_query


sample_text = article_query()['content'][0]
tt = "At the invitation of Jordan Customs, in its capacity as the new Vice-Chair for the WCO North of Africa, Near and Middle East (MENA) region, the WCO Secretary General, " \
     "Dr. Kunio Mikuriya, participated in the country’s virtual celebration of International Customs Day (ICD) on 26 January.<br/>In his opening remarks, Secretary General Mikuriya " \
     "praised Customs officers for their efforts, sometimes at the risk of their own lives, in protecting borders as well as ensuring the swift movement of medicines, " \
     "vaccines and other essential goods along the supply chain during this difficult period. He also congratulated Dr. Abdelmajid Alrahamneh on his election " \
     "as Vice-Chairperson of the WCO Council for the MENA region. He went on to explain the reasoning behind this year’s theme of “Customs bolstering Recovery, " \
     "Renewal and Resilience for a sustainable supply chain”, and what it means for the Customs community.<br/>Recovery can be sustained through greater collaboration between Customs and " \
     "its stakeholders. This can be achieved by means of enhanced Coordinated Border Management, including the Single Window approach. " \
     "The Customs community is encouraged to embrace technological advances and innovative approaches, such as blockchain technology or other concepts " \
     "that may support digitization of Customs processes, so as to ensure Renewal of the Customs system and the way the supply chain is currently set up. " \
     "It is also important for Customs to focus on Resilience by investing in people and their training, and by reviewing organizational policies to ensure they encompass integrity, " \
     "gender equality and diversity values. These measures will help improve the preparedness of people for pandemics and other unpredictable situations in the future." \
     "<br/>The meeting also saw the online and recorded interventions of Directors General of Customs in the region as well as the participation of business representatives. " \
     "After wishing everyone a happy ICD, Dr. Mikuriya concluded by affirming his trust in Jordan Customs’ ability to lead the way as regional Vice-Chair."
rake_result = rake_keyword_extract(tt)
spacy_result = spacy_keyword_extract(tt)
yake_result = yake_keyword_extract(tt)


print(rake_result)
print(spacy_result)
print(yake_result)

# if __name__ == "__main__":
#